# # num = 0
# a = 2
# b = a+1
#
# def tongji(num):
#     for i in [1, 2, 4, 6, 9, 34, 55]:
#         if i > 7:
#             num += 1
#     return num
#
# print(tongji(a))

# key不存在则返回value参数指定的值：
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.get("brand", 15000)

print(x)
print(car)



# a = ["导管", "导管", "导管", "乳"]
# di_head= {}
# for head in a:
#
#     tmp = di_head.get(head, 0)
#     di_head[head] = tmp + 1         #追加1个头实体head的个数记录,(当完成一段的属性填值以后)
#     print("tmp:   "+str(tmp))
#     print("di_head[head]:  "+str(di_head[head]))
