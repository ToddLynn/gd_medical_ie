"""
函数封装
"""

import re
import copy

B = {"增生腺体": {"增生_侧别": None, "增生_表现": None}, "导管": {"导管_侧别": None, "导管_表现": None},
     "病灶": {"病灶_侧别": None, "病灶_象限": None, "病灶_钟面": None, "病灶_评估分类": None, "病灶_回声强度": None, },
     "腋窝": {"腋窝_侧别": None, "腋窝_淋巴结表现": None, "腋窝_评估分类": None},
     "锁骨上侧": {"锁骨上侧_侧别": None, "锁骨上_淋巴结表现": None, "锁骨上_评估分类": None},
     "锁骨下侧": {"锁骨下_侧别": None, "锁骨下_淋巴结表现": None, "锁骨下_评估分类": None},
     "内乳": {"内乳_侧别": None, "内乳_淋巴结表现": None, "内乳_评估分类": None}}
D = copy.deepcopy(B)


def structured_output(output_dict):
    li_spo = output_dict["spo_list"]
    text = output_dict["text"]

    li_ss = re.split("[；。]", text)
    li_ss = [i for i in li_ss if i != '']

    # 遍历 五元组列表里的每一个元组
    li_head = []
    dict_head = {}
    tmp = 0
    # li_total_head = []

    "遍历  每一段分句"
    for sentence in li_ss:
        "遍历  每一条关系"
        for spo in li_spo:
            span = spo["object"]["@value"]  # "尾实体对应的文本-字词片段"

            attr = spo["predicate"]         # "尾实体对应的属性名"
            head = spo["subject_type"]      # "尾实体对应的头实体"

            tmp = dict_head.get(head, 0)    # 获取 -当前字典中头实体head的个数

            "如果词语在第一段句子中"
            if span in sentence:
                if tmp == 0:
                    D[head][attr] = span
                    li_head.append(head)
                else:
                    module = head + str(dict_head[head] + 1)
                    D[module] = B[head]
                    D[module][attr] = span
                    li_head.append(head)

        # 当  一段分句中的所有属性已经填满，把这个分句里的head添加到li_head里面。
        # head = list(set(li_head))[0]
        head = list(set(li_head))[0]
        # print(head)
        # print(list(set(li_head)))

        li_head = []

        dict_head[head] = tmp + 1  # 完成一段的书写，追加1个头实体head的个数记录


    return D

if __name__ == '__main__':
    pass
# output_dict = {
#     "spo_list": [
#         {
#             "object": {
#                 "@value": "双"
#             },
#             "object_type": {
#                 "@value": "侧别"
#             },
#             "predicate": "病灶_侧别",
#             "subject": "乳",
#             "subject_type": "病灶"
#         },
#         {
#             "object": {
#                 "@value": "左"
#             },
#             "object_type": {
#                 "@value": "侧别"
#             },
#             "predicate": "病灶_侧别",
#             "subject": "乳",
#             "subject_type": "病灶"
#         },
#         {
#             "object": {
#                 "@value": "无回声"
#             },
#             "object_type": {
#                 "@value": "回声强度"
#             },
#             "predicate": "病灶_回声强度",
#             "subject": "乳",
#             "subject_type": "病灶"
#         },
#         {
#             "object": {
#                 "@value": "低回声"
#             },
#             "object_type": {
#                 "@value": "回声强度"
#             },
#             "predicate": "病灶_回声强度",
#             "subject": "乳",
#             "subject_type": "病灶"
#         },
#         {
#             "object": {
#                 "@value": "BI-RADS3类"
#             },
#             "object_type": {
#                 "@value": "BI-RADS分类_超声"
#             },
#             "predicate": "病灶_评估分类",
#             "subject": "乳",
#             "subject_type": "病灶"
#         },
#         {
#             "object": {
#                 "@value": "BI-RADS2类"
#             },
#             "object_type": {
#                 "@value": "BI-RADS分类_超声"
#             },
#             "predicate": "病灶_评估分类",
#             "subject": "乳",
#             "subject_type": "病灶"
#         },
#         {
#             "object": {
#                 "@value": "左侧"
#             },
#             "object_type": {
#                 "@value": "侧别"
#             },
#             "predicate": "腋窝_侧别",
#             "subject": "腋下",
#             "subject_type": "腋窝"
#         },
#         {
#             "object": {
#                 "@value": "右侧"
#             },
#             "object_type": {
#                 "@value": "侧别"
#             },
#             "predicate": "腋窝_侧别",
#             "subject": "腋下",
#             "subject_type": "腋窝"
#         },
#         {
#             "object": {
#                 "@value": "未见明显淋巴结"
#             },
#             "object_type": {
#                 "@value": "淋巴结表现"
#             },
#             "predicate": "腋窝_淋巴结表现",
#             "subject": "腋下",
#             "subject_type": "腋窝"
#         },
#         {
#             "object": {
#                 "@value": "淋巴结肿大"
#             },
#             "object_type": {
#                 "@value": "淋巴结表现"
#             },
#             "predicate": "腋窝_淋巴结表现",
#             "subject": "腋下",
#             "subject_type": "腋窝"
#         }
#     ],
#     "text": "双乳低回声,BI-RADS3类。左乳无回声,BI-RADS2类。左侧腋下未见明显淋巴结；右侧腋下淋巴结肿大。"
# }

# print(structured_output(output_dict))
