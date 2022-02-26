import json
from tqdm import tqdm


# json_path = "./data/sc_train_406.json"
# json_path = "./data/duie_train_4000.json"
json_path = "./data/kt_train_406.json"


# """
# 测试json保存格式是否还会报错
# """
# with open(json_path, "r", encoding="utf-8") as fp:
#     lines = fp.readlines()
#     print(lines)
#     print(len(lines))
#     print("-"*110)
#
#
#
# examples = []
# tokenized_examples = []
#
#
# for line in tqdm(lines):
#     example = json.loads(line)
#
#     spo_list = example['spo_list'] if "spo_list" in example.keys() else []
#
#
#     text_raw = example['text']
#
#     # print("*"*100)
#
#
# with open("./data/predicate2id.json", 'r', encoding='utf8') as fp:
#     label_map = json.load(fp)

"""
debug
"""
with open("data/predicate2id.json", 'r', encoding='utf8') as fp:
    label_map = json.load(fp)

num_labels = 2 * (len(label_map.keys()) - 2) + 2
print(label_map.keys())
print(num_labels)

