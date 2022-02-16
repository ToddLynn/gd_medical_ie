import os
import json




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


if __name__ == '__main__':
    golden_file = "./data/duie_dev.json"
    predict_file = "./output/eval_predictions.json"
    get_precision_recall_f1(golden_file, predict_file)
