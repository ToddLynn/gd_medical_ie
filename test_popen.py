# import os
# result = os.popen('ipconfig')
# # 返回的结果是一个<class 'os._wrap_close'>对象，需要读取后才能处理
# context = result.read()
# for line in context.splitlines():
#     print(line)
# result.close()


import os

golden_file = "data/duie_dev.json"
predict_file = "output/eval_predictions.json"

result = os.popen('python3 ./re_official_evaluation.py --golden_file={} --predict_file={}'.
                    format(golden_file, predict_file))
# 返回的结果是一个<class 'os._wrap_close'>对象，需要读取后才能处理
context = result.read()
for line in context.splitlines():
    print(line)
result.close()