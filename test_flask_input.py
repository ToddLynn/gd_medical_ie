import json
from predict import *

def get_str():
    import json

    # 1、获取到的str，保存为本地
    str1 = "乔丹，双侧乳腺组织增生，左侧腋下淋巴结明显肿大"
    dict1 = {}
    dict1["text"] = str1
    inputpath = "data/input/kt_input1.json"
    with open(inputpath, "w", encoding="utf-8") as fp:
        json.dump(dict1, fp, ensure_ascii=False)

    predict_re()


get_str()