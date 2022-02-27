import json

path1 = r"F:\workspace_dl_env\gd_medical_ie\output\test_predictions.json"


with open(path1, 'r',encoding="utf-8") as load_f:
    load_dict = json.load(load_f)
    print(load_dict)
