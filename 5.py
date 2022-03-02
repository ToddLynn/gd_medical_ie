#
# # di = {}
# # di["key1"] = "value"
# # print(di)
#
# """
# 验证字典里的元素是否可以复制--可以复制
# """
# di_2 = {
#     "A":{
#         "a1":None,"a2":None
#     }
# }
#
# di_2["B"]= di_2["A"]
# print(di_2)
#
# """
# 验证硬拷贝、软拷贝
# """
# # # di_3 = di_2
# # di_2["A"]["a2"] = 555
# # print(di_2)
# # # print(di_3)

# import copy
#
# a = {"k":113,"o":555}
#
# d = copy.deepcopy(a)
# d["k"] = 142
# print(a)
# print(d)


head="乳腺"
dict_head = {}
a = dict_head[head]
