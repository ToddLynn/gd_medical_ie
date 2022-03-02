# num = 0
a = 2
b = a+1

def tongji(num):
    for i in [1, 2, 4, 6, 9, 34, 55]:
        if i > 7:
            num += 1
    return num

print(tongji(a))