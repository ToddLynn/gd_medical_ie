"""
@Time : 2021/2/78:58
@Auth : 周俊贤
@File ：utils.py
@DESCRIPTION:

"""
from flask import Flask, jsonify

import codecs
import json
import logging
import os
import random
import re
import time
import zipfile
from pathlib import Path

import numpy as np
import torch


def seed_everything(seed=1029):
    '''
    设置整个开发环境的seed
    :param seed:
    :param device:
    :return:
    '''
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    # some cudnn methods can be random even after fixing the seed
    # unless you tell it to be deterministic
    torch.backends.cudnn.deterministic = True


class ProgressBar(object):
    '''
    custom progress bar
    Example:
        >>> pbar = ProgressBar(n_total=30,desc='training')
        >>> step = 2
        >>> pbar(step=step)
    '''

    def __init__(self, n_total, width=30, desc='Training'):
        self.width = width
        self.n_total = n_total
        self.start_time = time.time()
        self.desc = desc

    def __call__(self, step, info={}):
        now = time.time()
        current = step + 1
        recv_per = current / self.n_total
        bar = f'[{self.desc}] {current}/{self.n_total} ['
        if recv_per >= 1:
            recv_per = 1
        prog_width = int(self.width * recv_per)
        if prog_width > 0:
            bar += '=' * (prog_width - 1)
            if current < self.n_total:
                bar += ">"
            else:
                bar += '='
        bar += '.' * (self.width - prog_width)
        bar += ']'
        show_bar = f"\r{bar}"
        time_per_unit = (now - self.start_time) / current
        if current < self.n_total:
            eta = time_per_unit * (self.n_total - current)
            if eta > 3600:
                eta_format = ('%d:%02d:%02d' %
                              (eta // 3600, (eta % 3600) // 60, eta % 60))
            elif eta > 60:
                eta_format = '%d:%02d' % (eta // 60, eta % 60)
            else:
                eta_format = '%ds' % eta
            time_info = f' - ETA: {eta_format}'
        else:
            if time_per_unit >= 1:
                time_info = f' {time_per_unit:.1f}s/step'
            elif time_per_unit >= 1e-3:
                time_info = f' {time_per_unit * 1e3:.1f}ms/step'
            else:
                time_info = f' {time_per_unit * 1e6:.1f}us/step'

        show_bar += time_info
        if len(info) != 0:
            show_info = f'{show_bar} ' + \
                        "-".join([f' {key}: {value:.4f} ' for key, value in info.items()])
            print(show_info, end='')
        else:
            print(show_bar, end='')


logger = logging.getLogger()


def init_logger(log_file=None, log_file_level=logging.NOTSET):
    '''
    Example:
        >>> init_logger(log_file)
        >>> logger.info("abc'")
    '''
    if isinstance(log_file, Path):
        log_file = str(log_file)
    log_format = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                                   datefmt='%m/%d/%Y %H:%M:%S')

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.handlers = [console_handler]
    if log_file and log_file != '':
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_file_level)
        # file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)
    return logger


def find_entity(text_raw,
                id_,
                predictions,
                offset_mapping):
    """
    retrieval entity mention under given predicate id for certain prediction.
    this is called by the "decoding" func.
    """
    entity_list = []
    for i in range(len(predictions)):
        if [id_] in predictions[i]:
            j = 0
            while i + j + 1 < len(predictions):  # 超过序列的长度
                if [1] in predictions[i + j + 1]:
                    j += 1
                else:
                    break
            entity = ''.join(text_raw[offset_mapping[i][0]:
                                      offset_mapping[i + j][1]])
            entity_list.append(entity)
    return list(set(entity_list))


def decoding(example_all,
             id2spo,
             logits_all,
             seq_len_all,
             offset_mapping_all
             ):
    """
    model output logits -> formatted spo (as in data set file)
    """
    formatted_outputs = []
    for (i, (example, logits, seq_len, offset_mapping)) in \
            enumerate(zip(example_all, logits_all, seq_len_all, offset_mapping_all)):
        logits = logits[1:seq_len - 2 + 1]  # slice between [CLS] and [SEP] to get valid logits
        logits[logits >= 0.5] = 1
        logits[logits < 0.5] = 0
        offset_mapping = offset_mapping[1:seq_len - 2 + 1]
        predictions = []
        for token in logits:
            predictions.append(np.argwhere(token == 1).tolist())

        # format predictions into example-style output
        formatted_instance = {}
        text_raw = example['text']
        # complex_relation_label = [8, 10, 26, 32, 46]
        # complex_relation_affi_label = [9, 11, 27, 28, 29, 33, 47]

        complex_relation_label = [12, 15, 18, 21]
        complex_relation_affi_label = [6, 7, 8, 9, 10, 13, 16, 19, 22]

        # flatten predictions then retrival all valid subject id
        # 展平预测，然后检索所有有效的 头实体id

        flatten_predictions = []
        for layer_1 in predictions:
            for layer_2 in layer_1:
                flatten_predictions.append(layer_2[0])
        subject_id_list = []
        for cls_label in list(set(flatten_predictions)):
            # if 1 < cls_label <= 56 and (cls_label + 55) in flatten_predictions:

            if 1 < cls_label <= 22 and (cls_label + 21) in flatten_predictions:
                subject_id_list.append(cls_label)
        subject_id_list = list(set(subject_id_list))

        # fetch all valid spo by subject id
        # 按头实体id  获取所有有效的spo
        spo_list = []
        for id_ in subject_id_list:
            if id_ in complex_relation_affi_label:
                continue  # do this in the next "else" branch
            if id_ not in complex_relation_label:
                subjects = find_entity(text_raw,
                                       id_,
                                       predictions,
                                       offset_mapping)
                objects = find_entity(text_raw,
                                      # id_ + 55,
                                      id_ + 21,
                                      predictions,
                                      offset_mapping)
                for subject_ in subjects:
                    for object_ in objects:
                        spo_list.append({
                            "predicate": id2spo['predicate'][id_],
                            "object_type": {'@value': id2spo['object_type'][id_]},
                            'subject_type': id2spo['subject_type'][id_],
                            "object": {'@value': object_},
                            "subject": subject_
                        })
            else:
                #  traverse all complex relation and look through their corresponding affiliated objects
                #  遍历所有复杂的关系，查看它们对应的附属对象
                subjects = find_entity(text_raw,
                                       id_,
                                       predictions,
                                       offset_mapping)
                objects = find_entity(text_raw,
                                      # id_ + 55,
                                      id_ + 21,
                                      predictions,
                                      offset_mapping)
                for subject_ in subjects:
                    for object_ in objects:
                        object_dict = {'@value': object_}
                        object_type_dict = {'@value': id2spo['object_type'][id_].split('_')[0]}
                        # if id_ in [8, 10, 32, 46] and id_ + 1 in subject_id_list:

                        if id_ in [12, 15, 18, 21] and id_ + 1 in subject_id_list:
                            id_affi = id_ + 1
                            object_dict[id2spo['object_type'][id_affi].split(
                                '_')[1]] = find_entity(text_raw,
                                                       # id_affi + 55,
                                                       id_affi + 21,
                                                       predictions,
                                                       offset_mapping)[0]
                            object_type_dict[id2spo['object_type'][id_affi].split('_')[1]] = \
                                id2spo['object_type'][id_affi].split('_')[0]

                        elif id_ == 6:
                            # for id_affi in [27, 28, 29]:

                            for id_affi in [7, 8, 9, 10]:
                                if id_affi in subject_id_list:
                                    object_dict[id2spo['object_type'][id_affi].split('_')[1]] = \
                                        find_entity(text_raw,
                                                    # id_affi + 55,
                                                    id_affi + 21,
                                                    predictions,
                                                    offset_mapping)[0]
                                    object_type_dict[id2spo['object_type'][id_affi].split('_')[1]] = \
                                        id2spo['object_type'][id_affi].split('_')[0]
                        spo_list.append({
                            "predicate": id2spo['predicate'][id_],
                            "object_type": object_type_dict,
                            "subject_type": id2spo['subject_type'][id_],
                            "object": object_dict,
                            "subject": subject_
                        })

        formatted_instance['text'] = example['text']
        formatted_instance['spo_list'] = spo_list
        formatted_outputs.append(formatted_instance)

    return formatted_outputs


def write_prediction_results(formatted_outputs, file_path):
    """write the prediction results"""

    with codecs.open(file_path, 'w', 'utf-8') as f:
        for formatted_instance in formatted_outputs:
            json_str = json.dumps(formatted_instance, ensure_ascii=False)
            f.write(json_str)
            f.write('\n')
        # zipfile_path = file_path + '.zip'
        # f = zipfile.ZipFile(zipfile_path, 'w', zipfile.ZIP_DEFLATED)
        # f.write(file_path)

    # return zipfile_path

    # #flask
    # app = Flask(__name__)
    # @app.route('/medical_ie')
    # def get_messages():
    #     return jsonify({"medical_ie":formatted_outputs})
    # app.config["JSON_AS_ASCII"] = False
    # app.run(port= 8080)


def get_precision_recall_f1(golden_file, predict_file):
    r = os.popen(
        'python ./re_official_evaluation.py --golden_file={} --predict_file={}'.
            format(golden_file, predict_file))
    result = r.read()
    print("test", result)
    r.close()
    d_result = json.loads(result)
    precision = d_result["precision"]
    recall = d_result["recall"]
    f1 = d_result["f1-score"]

    return precision, recall, f1
