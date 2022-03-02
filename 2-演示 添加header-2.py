li = []
a = ["导管", "导管", "乳", "乳"]
di_head = {}
for head in a:

    tmp = di_head.get(head, 0)      #获取 -当前字典里头实体head的个数

    di_head[head] = tmp + 1         #追加1个头实体head的个数记录,(当完成一段的属性填值以后)

    module_name = head + str(di_head[head])  #当前模块名的定义，导管，导管1

    # print(tmp)
    # print(di_head[head])
    print(module_name)

    # print(module_name.replace('1', ''))
    # print(di_head)
"""
解决的是，模块名称的追加问题
导管
导管2
导管3
乳
"""

di_head = {}
head ="腋窝"
aaa = di_head.get(head,0)
print(aaa)