"""
函数封装
"""

import re
import copy

B = {"增生腺体": {"增生_侧别": None, "增生_表现": None}, "导管": {"导管_侧别": None, "导管_表现": None},
     "病灶": {"病灶_侧别": None, "病灶_象限": None, "病灶_钟面": None, "病灶_评估分类": None, "病灶_回声强度": None, },
     "腋窝": {"腋窝_侧别": None, "腋窝_淋巴结表现": None, "腋窝_评估分类": None},
     "锁骨上侧": {"锁骨上侧_侧别": None, "锁骨上_淋巴结表现": None, "锁骨上_评估分类": None},
     "锁骨下侧": {"锁骨下_侧别": None, "锁骨下_淋巴结表现": None, "锁骨下_评估分类": None},
     "内乳": {"内乳_侧别": None, "内乳_淋巴结表现": None, "内乳_评估分类": None}}
D =copy.deepcopy(B)

dict_input = {"code": 200, "data": {"spo_list": [
    {"object": {"@value": "右侧", "index": "[12,13]"}, "object_type": {"@value": "侧别"}, "predicate": "腋窝_侧别",
     "subject": "腋下", "subject_type": "腋窝"},
    {"object": {"@value": "左侧", "index": "[0,1]"}, "object_type": {"@value": "侧别"}, "predicate": "腋窝_侧别",
     "subject": "腋下", "subject_type": "腋窝"},
    {"object": {"@value": "淋巴结肿大", "index": "[16,20]"}, "object_type": {"@value": "淋巴结表现"}, "predicate": "腋窝_淋巴结表现",
     "subject": "腋下", "subject_type": "腋窝"},
    {"object": {"@value": "未见明显淋巴结", "index": "[4,10]"}, "object_type": {"@value": "淋巴结表现"}, "predicate": "腋窝_淋巴结表现",
     "subject": "腋下", "subject_type": "腋窝"}], "text": "左侧腋下未见明显淋巴结；右侧腋下淋巴结肿大。"}, "msg": "success"}
li_spo = dict_input["data"]["spo_list"]

text = "左侧腋下未见明显淋巴结；右侧腋下淋巴结肿大。"

# 分段

li_ss = re.split("[；。]", text)
li_ss = [i for i in li_ss if i != '']
# print(li_ss)

# # 判断尾实体是否在第1段话里
#
# # 第一段话
# sentence_1 = li_ss[0]
#
# # 判断尾实体是否在第1段话里
#
# 遍历 五元组列表里的每一个元组
li_head = []
di_head = {}
tmp = 0
#todo 每一个句子
for sentence in li_ss:

    #todo 对于每一条关系
    for o in li_spo:
        span = o["object"]["@value"]  # "尾实体对应的文本-字词片段"

        attr = o["predicate"]  # "尾实体对应的属性名"
        head = o["subject_type"]  # "尾实体对应的头实体"


#         #todo  如果词语在第一段句子中
        if span in sentence:
            if tmp == 0 :
                D[head][attr] = span
            else :
                module = head + str(di_head[head]+1)
                D[module] = B[head]
                D[module][attr] = span
    li_head.append(head)
    tmp = di_head.get(head, 0) +1  # 获取 -当前字典里头实体head的个数
    print("tmp:"+str(tmp))
    di_head[head] = tmp   # 完成一段的书写，追加1个头实体head的个数记录

print(li_head)
print(tmp)
print(D)
print(di_head)
#处理追加模块-2的代码
