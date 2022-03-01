import json
import os

output_dict = {
    "病灶": {
        "病灶_侧别": "左侧",
        "病灶_象限": "外上象限",
        "病灶_钟面": None,
        "病灶_评估分类": "3类",
        "病灶_回声强度": None
    },
    "病灶2": {
        "病灶_侧别": "右侧",
        "病灶_象限": None,
        "病灶_钟面": "9点",
        "病灶_评估分类": "4A类",
        "病灶_回声强度": "低回声"
    }
}
D = {
    "增生腺体": {
        "增生_侧别": None,
        "增生_表现": None
    },
    "导管": {
        "导管_侧别": None,
        "导管_表现": None
    },
    "病灶": {
        "病灶_侧别": None,
        "病灶_象限": None,
        "病灶_钟面": None,
        "病灶_评估分类": None,
        "病灶_回声强度": None,
    },
    "腋窝": {
        "腋窝_侧别": None,
        "腋窝_淋巴结表现": None,
        "腋窝_评估分类": None
    },
    "锁骨上侧": {
        "锁骨上侧_侧别": None,
        "锁骨上_淋巴结表现": None,
        "锁骨上_评估分类": None
    },
    "锁骨下侧": {
        "锁骨下_侧别": None,
        "锁骨下_淋巴结表现": None,
        "锁骨下_评估分类": None
    },
    "内乳": {
        "内乳_侧别": None,
        "内乳_淋巴结表现": None,
        "内乳_评估分类": None
    }
}
# content = "左侧腋下淋巴结肿大。右侧腋下未见明显肿大淋巴结。"
# input_dict = {"spo_list": [
#     {"object": {"@value": "右侧"}, "object_type": {"@value": "侧别"}, "predicate": "腋窝_侧别", "subject": "腋下",
#      "subject_type": "腋窝"},
#     {"object": {"@value": "未见明显肿大淋巴结"}, "object_type": {"@value": "淋巴结表现"}, "predicate": "腋窝_淋巴结表现", "subject": "腋下",
#      "subject_type": "腋窝"},
#     {"object": {"@value": "右侧"}, "object_type": {"@value": "侧别"}, "predicate": "腋窝_侧别", "subject": "腋下",
#      "subject_type": "腋窝"},
#     {"object": {"@value": "淋巴结肿大"}, "object_type": {"@value": "淋巴结表现"}, "predicate": "腋窝_淋巴结表现", "subject": "腋下",
#      "subject_type": "腋窝"}], "text": "左侧腋下淋巴结肿大。右侧腋下未见明显肿大淋巴结。"}
content = "2、左乳外上象限结节，考虑BI-RADS3类。3、右乳9点低回声,性质待定,BI-RADS4A类。"

input_dict_2 = {"text": "左乳外上象限结节，考虑BI-RADS3类。3、右乳9点低回声,性质待定,BI-RADS4A类。", "spo_list": [
    {"predicate": "病灶_侧别", "object_type": {"@value": "侧别"}, "subject_type": "病灶", "object": {"@value": "左侧"},
     "subject": "乳"},
    {"predicate": "病灶_象限", "object_type": {"@value": "象限定位"}, "subject_type": "病灶", "object": {"@value": "外上象限"},
     "subject": "乳"}, {"predicate": "病灶_评估分类", "object_type": {"@value": "BI-RADS分类_超声"}, "subject_type": "病灶",
                       "object": {"@value": "BI-RADS3类"}, "subject": "乳"},
    {"predicate": "病灶_侧别", "object_type": {"@value": "侧别"}, "subject_type": "病灶", "object": {"@value": "右"},
     "subject": "乳"},
    {"predicate": "病灶_钟面", "object_type": {"@value": "钟面定位"}, "subject_type": "病灶", "object": {"@value": "9点"},
     "subject": "乳"},
    {"predicate": "病灶_回声强度", "object_type": {"@value": "回声强度"}, "subject_type": "病灶", "object": {"@value": "低回声"},
     "subject": "乳"}, {"predicate": "病灶_评估分类", "object_type": {"@value": "BI-RADS分类_超声"}, "subject_type": "病灶",
                       "object": {"@value": "BI-RADS4A类"}, "subject": "乳"}, ]}

list_d = input_dict_2['spo_list']
print(list_d)