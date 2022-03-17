"""模型输出spo_list后处理"""
"""把输出的作为病灶的"乳腺组织"改为"乳"""



import json

# 一、读取test_predictions.json
"""对单条content的output_model的病灶值，用(乳)替换(乳腺组织)"""
def head_value_replace():
    path = "./output/test_predictions.json"

    with open(path, "r", encoding="utf-8") as fr:
        dict1 = json.load(fr)

    # print(dict1)

    for spo in dict1["spo_list"]:
        if spo["subject_type"] == "病灶":
            spo["subject"] = "乳"

    with open(path, "w", encoding="utf-8") as fw:
        json.dump(dict1, fw, ensure_ascii=False)


"""对多条content的output_model的病灶值，用(乳)替换(乳腺组织)"""
