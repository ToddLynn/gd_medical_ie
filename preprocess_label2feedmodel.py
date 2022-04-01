import json
import os

# file_json = r"D:\home\GdLabel\data250-third-20220331-0930-relation.json"



dir_name = r"E:\02-pre_research\知识图谱\数据集\乳腺超声检查报告_labeled\20220331_2"
li_dir = os.listdir(dir_name)

# new_path = r"data/kt_train_713.json"
new_path = r"data/load_data_20220401.json"

if os.path.exists(new_path):
    os.remove(new_path)


for dir in li_dir:
    path_json  =os.path.join(dir_name,dir)

    """读取json文件放到list里面"""
    with open(path_json, "r", encoding="utf-8") as fb:
        li_json = json.load(fb)





    with open(new_path, "a", encoding="utf-8") as fp:
        for line in li_json:
            if line["spo_list"]:

                for d in line["spo_list"]:
                    d["object"].pop("id")
                print(line)
                print("="*100)

                str1 = json.dumps(line, ensure_ascii=False)
                fp.write(str1 + "\n")