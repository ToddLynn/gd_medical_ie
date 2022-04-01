str1 = "1、双侧乳腺组织增生。双侧乳腺多发囊性结节,BI-RADS3类,建议定期复查。2、双侧腋下未见明显肿大淋巴结。"

# aaa =str1.find("BI-RADS3类")
aaa =str1.find("腋下")
seg =str1.find("2、双侧腋下未见明显肿大淋巴结。")
print("2、双侧腋下未见明显肿大淋巴结。",seg)


bbb =str1.find("双侧")
print("双侧   :",bbb)


ccc = str1.find("双侧",seg)
ddd = str1.find("腋下",seg)
eee = str1.find("未见明显肿大淋巴结",seg)

print("双侧   :",ccc)
print("腋下   :",ddd)
print("未见明显肿大淋巴结   :",eee)


{"text": "1、双侧乳腺组织增生,BI-RADS2类。2、双腋下未见明显肿大淋巴结。请结合临床,定期复查！", "spo_list": [{"subject": "双", "subject_id": 7, "object": {"@value": "乳腺组织", "id": 6}, "predicate": "腋窝_淋巴结表现", "subject_type": "侧别", "object_type": {"@value": "增生腺体"}}, {"subject": "乳", "subject_id": 9, "object": {"@value": "双", "id": 8}, "predicate": "增生_侧别", "subject_type": "病灶", "object_type": {"@value": "侧别"}}, {"subject": "BI-RADS2类", "subject_id": 3, "object": {"@value": "双", "id": 8}, "predicate": "增生_表现", "subject_type": "BI-RADS分类_超声", "object_type": {"@value": "侧别"}}], "entities": [{"start_idx": 8, "end_idx": 10, "type": "乳腺组织改变", "entity": "增生", "id": 1}, {"start_idx": 11, "end_idx": 20, "type": "BI-RADS分类_超声", "entity": "BI-RADS2类", "id": 3}, {"start_idx": 24, "end_idx": 26, "type": "腋窝", "entity": "腋下", "id": 4}, {"start_idx": 26, "end_idx": 35, "type": "淋巴结表现", "entity": "未见明显肿大淋巴结", "id": 5}, {"start_idx": 4, "end_idx": 8, "type": "增生腺体", "entity": "乳腺组织", "id": 6}, {"start_idx": 2, "end_idx": 3, "type": "侧别", "entity": "双", "id": 7}, {"start_idx": 23, "end_idx": 24, "type": "侧别", "entity": "双", "id": 8}, {"start_idx": 4, "end_idx": 5, "type": "病灶", "entity": "乳", "id": 9}]}