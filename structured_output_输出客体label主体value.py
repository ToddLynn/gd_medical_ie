"""
函数封装
"""

import re
import copy




def structured_output_label(output_dict):
    B =    {
        "增生腺体": {
            "增生_侧别": {},
            "增生_表现": {}
        },
        "导管": {
            "导管_侧别": {},
            "导管_表现": {}
        },
        "病灶": {
            "病灶_侧别": {},
            "病灶_象限": {},
            "病灶_钟面": {},
            "病灶_评估分类": {},
            "病灶_回声强度": {},

        },
        "腋窝": {
            "腋窝_侧别": {},
            "腋窝_淋巴结表现": {},
            "腋窝_评估分类": {}
        },
        "锁骨上侧": {
            "锁骨上侧_侧别": {},
            "锁骨上_淋巴结表现": {},
            "锁骨上_评估分类": {}
        },
        "锁骨下侧": {
            "锁骨下_侧别": {},
            "锁骨下_淋巴结表现": {},
            "锁骨下_评估分类": {}
        },
        "内乳": {
            "内乳_侧别": {},
            "内乳_淋巴结表现": {},
            "内乳_评估分类": {}
        }
    }

    D = copy.deepcopy(B)
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
            label = spo["object_type"]["@value"]     # "尾实体对应的头实体"

            tmp = dict_head.get(head, 0)    # 获取 -当前字典中头实体head的个数

            "如果字词片段span 在第一段句子中"
            if span in sentence:
                if tmp == 0:
                    d = D[head]
                    # d[attr]["entity"] = span
                    # d[attr]["label"] = label
                    # li_head.append(head)
                else:
                    module = head + str(dict_head[head] + 1)
                    D[module] = B[head]
                    d = D[module]
                d[attr]["entity"] = span
                d[attr]["label"] = label
                d[attr]["idx"] = [text.find(span),text.find(span)+len(span)]



                li_head.append(head)

        # 当  一段分句中的所有属性已经填满，把这个分句里的head添加到li_head里面。
        # head = list(set(li_head))[0]
        # print(list(set(li_head)))
        try:
            head = list(set(li_head))[0]
            # print(head)
            # print(list(set(li_head)))


            li_head = []

            dict_head[head] = tmp + 1  # 完成一段的书写，追加1个头实体head的个数记录
        except:
            # print("\n"+"-"*100)
            # print("li_head = []")
            pass


    return D


if __name__ == '__main__':
    dict1 = {"text": "1、左乳外上象限巨大低回声团,考虑BI-RADS:5类。2、右乳内上象限，BI-RADS2类。3、双侧腋下未见明显肿大淋巴结。", "spo_list": [
        {"predicate": "病灶_侧别", "object_type": {"@value": "侧别"}, "subject_type": "病灶", "object": {"@value": "右"},
         "subject": "乳"},
        {"predicate": "病灶_侧别", "object_type": {"@value": "侧别"}, "subject_type": "病灶", "object": {"@value": "左"},
         "subject": "乳"},
        {"predicate": "病灶_象限", "object_type": {"@value": "象限定位"}, "subject_type": "病灶", "object": {"@value": "内上象限"},
         "subject": "乳"},
        {"predicate": "病灶_象限", "object_type": {"@value": "象限定位"}, "subject_type": "病灶", "object": {"@value": "外上象限"},
         "subject": "乳"}, {"predicate": "病灶_评估分类", "object_type": {"@value": "BI-RADS分类_超声"}, "subject_type": "病灶",
                           "object": {"@value": "BI-RADS2类"}, "subject": "乳"},
        {"predicate": "病灶_评估分类", "object_type": {"@value": "BI-RADS分类_超声"}, "subject_type": "病灶",
         "object": {"@value": "BI-RADS:5类"}, "subject": "乳"},
        {"predicate": "腋窝_侧别", "object_type": {"@value": "侧别"}, "subject_type": "腋窝", "object": {"@value": "双侧"},
         "subject": "腋下"}, {"predicate": "腋窝_淋巴结表现", "object_type": {"@value": "淋巴结表现"}, "subject_type": "腋窝",
                            "object": {"@value": "未见明显肿大淋巴结"}, "subject": "腋下"}]}

    result = structured_output_label(dict1)

    print(result)

    # dict_target =    {
    #     "text": "1、左乳外上象限巨大低回声团,考虑BI-RADS:5类。2、右乳内上象限，BI-RADS2类。3、双侧腋下未见明显肿大淋巴结。",
    #     "output_dict": {
    #         "内乳": {
    #             "内乳_侧别": None,
    #             "内乳_淋巴结表现": None,
    #             "内乳_评估分类": None
    #         },
    #         "增生腺体": {
    #             "增生_侧别": None,
    #             "增生_表现": None
    #         },
    #         "导管": {
    #             "导管_侧别": None,
    #             "导管_表现": None
    #         },
    #         "病灶": {
    #             "主体": {"value": "乳", "idx": [3, 4], "type": "病灶"},
    #             "病灶_侧别": {"value": "左", "idx": [2, 3], "type": "侧别"},
    #             "病灶_回声强度": None,
    #             "病灶_评估分类": {"value": "BI-RADS:5类", "idx":    [17, 27], "type": "BI-RADS分类_超声"},
    #             "病灶_象限": {"value": "外上象限", "idx": [4, 8], "type": "象限定位"},
    #             "病灶_钟面": None
    #         },
    #         "病灶2": {
    #             "主体": {"value": "乳", "idx": [31, 32], "type": "病灶"},
    #             "病灶_侧别": {"value": "右", "idx": [30, 31], "type": "侧别"},
    #             "病灶_回声强度": None,
    #             "病灶_评估分类": {"value": "BI-RADS2类", "idx": [37, 46], "type": "BI-RADS分类_超声"},
    #             "病灶_象限": {"value": "内上象限", "idx": [32, 36], "type": "象限定位"},
    #             "病灶_钟面": None
    #         },
    #         "腋窝": {
    #             "主体": {"value": "腋下", "idx": [51, 53], "type": "腋窝"},
    #             "腋窝_侧别": {"value": "双侧", "idx": [49, 51], "type": "病灶"},
    #             "腋窝_淋巴结表现": {"value": "未见明显肿大淋巴结", "idx": [53, 62], "type": "病灶"},
    #             "腋窝_评估分类": None
    #         },
    #         "锁骨上侧": {
    #             "锁骨上_淋巴结表现": None,
    #             "锁骨上_评估分类": None,
    #             "锁骨上侧_侧别": None
    #         },
    #         "锁骨下侧": {
    #             "锁骨下_侧别": None,
    #             "锁骨下_淋巴结表现": None,
    #             "锁骨下_评估分类": None
    #         }
    #     }
    # }



