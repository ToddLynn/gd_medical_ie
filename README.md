# 项目说明:


# 依赖包
- python=3.6
- torch=1.7
```
 (conda环境下)- pip install -r requirements.txt
```
# 运行
启动  
```
python app_struct_show.py
--max_len=150 --model_name_or_path="./data/zhoujx/prev_trained_model/chinese_roberta_wwm_ext_pytorch" --per_gpu_eval_batch_size=2 --output_dir="./output" --fine_tunning_model="./output/best_model.pkl"
```




# 展示示例
```
1、双侧乳腺组织呈增生改变。2、右侧腋下未见明显肿大淋巴结。
1、左乳外上象限巨大低回声团,考虑BI-RADS:5类。2、右乳BI-RADS2类。3、双侧腋下未见明显肿大淋巴结。
1、双侧乳腺组织增生。2、左侧乳腺2点极低回声:BI-RADS3类。3、右侧腋下淋巴结可见。
1、双侧乳腺组织增生。BI-RADS3类。右乳导管局限性扩张。 2、左侧腋下未见明显肿大淋巴结。
1、双侧乳腺组织增生。2、左乳低回声结节,BI-RADS3类。3、右乳多发囊性暗区,BI-RADS2类。
```










#注意
1.乳腺组织增生描述、与乳腺BI-RADS分级的描述文本，暂不可同时识别。
2.右乳、右腋。没法区分右
