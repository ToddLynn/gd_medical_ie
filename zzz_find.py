str1 =  "1、左乳外上象限巨大低回声团,考虑BI-RADS:5类。2、右乳内上象限，BI-RADS2类。3、双侧腋下未见明显肿大淋巴结。"

# idx1 = str1.find("内",4)
# idx1 = str1.find("1")
# idx1 = str1.find("双")

idx1 = str1.find("未见明显肿大淋巴结",37)

print(idx1)

