import json
import os

# 1. 读取输出的json结果
output_path = r"output/test_predictions.json"

# 1.1 校验是否存在
if os.path.exists(output_path):
    # 1.2 读取json 放到dict变量里
    with open(output_path, "r", encoding="utf-8") as ft:
        dict_output = json.load(ft)
        # print(dict_output)
    # 1.3 校验dict 中"spo_list"是否为空列表
    if dict_output["spo_list"]:
        print(dict_output)
    else:
        print("spo列表为空列表")
    # 2.分组

    # 2.1 先定义一个标准格式
    D = {
        "乳腺组织": {
            "侧别": None,
            "表现": None
        },
        "导管": {
            "侧别": None,
            "表现": None
        },
        "病灶": {
            "侧别": None,
            "象限定位": None,
            "钟表定位": None,
            "乳腺病灶评估分类": None,
            "回声强度": None,
        },
        "淋巴结_腋窝": {
            "侧别": None,
            "淋巴结表现": None,
            "淋巴结评估分类": None
        },
        "淋巴结_锁骨上": {
            "侧别": None,
            "淋巴结表现": None,
            "淋巴结评估分类": None
        },
        "淋巴结_锁骨下": {
            "侧别": None,
            "淋巴结表现": None,
            "淋巴结评估分类": None
        },
        "淋巴结_内乳": {
            "侧别": None,
            "淋巴结表现": None,
            "淋巴结评估分类": None
        }
    }

    # 2.2 用标准格式 去过dict结果。有则填值，则置空
    list_d = dict_output['spo_list']

    # dict_map=
    list_relation = ["增生_侧别", "增生_表现", "导管_侧别", "导管_表现", "病灶_侧别", "病灶_象限",
                     "病灶_钟面", "病灶_回声强度", "病灶_评估分类", "腋窝_侧别", "腋窝_淋巴结表现", "腋窝_评估分类", "锁骨上侧_侧别",
                     "锁骨上_淋巴结表现", "锁骨上_评估分类", "锁骨下_侧别", "锁骨下_淋巴结表现", "锁骨下_评估分类", "内乳_侧别",
                     "内乳_淋巴结表现", "内乳_评估分类"]

    for d in list_d:
        if d["predicate"] in list_relation:
            pass

    # 3.输出分组后的json结果，传给flask post,同时在json.dump成另一个json本地文件













else:
    print("没有output.json文件")
