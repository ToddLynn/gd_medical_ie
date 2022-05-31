# Docker image for gd_medical_ie
# VERSION 1.0
# Author: Zengshulin
# 基础镜像使用python:3.6

FROM python:3.6-slim-buster
# 将服务器 requirements.txt 文件复制到 容器 /app/目录下
ADD . /app/
# 指定容器工作目录为 /app/
WORKDIR /app/
# 安装 项目依赖
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 运行
CMD ["python","app_struct_show.py"]
#CMD ['python','app_struct_show.py --max_len=150 --model_name_or_path="./data/zhoujx/prev_trained_model/chinese_roberta_wwm_ext_pytorch" --per_gpu_eval_batch_size=2 --output_dir="./output" --fine_tunning_model="./output/best_model.pkl ']

# 编译
# docker build -t image_medical_ie:v1 .
# docker build -t image_medical_ie_0526:v1 .

# run
# docker run -p 9090:8080 --name container_medical_ie image_medical_ie:v1
# docker run -p 9090:8080 --name container_medical_ie_0526 --max_len=150 --model_name_or_path="./data/zhoujx/prev_trained_model/chinese_roberta_wwm_ext_pytorch" --per_gpu_eval_batch_size=2 --output_dir="./output" --fine_tunning_model="./output/best_model.pkl" image_medical_ie_0526:v1