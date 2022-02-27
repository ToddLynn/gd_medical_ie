import json

# 1. 读取输出的json结果
output_path = r"F:\workspace_dl_env\gd_medical_ie\output\test_predictions.json"
with open(output_path, "r", encoding="utf-8") as ft:
    dict_output = json.load(ft)
    print(dict_output)
# 1.1 校验是否存在

# 1.2 读取json 放到dict变量里

# 2.分组
# 2.1 先定义一个标准格式

# 2.2 用标准格式 去过dict结果。有则填值，则置空

# 3.输出分组后的json结果，传给flask post,同时在json.dump成另一个json本地文件
