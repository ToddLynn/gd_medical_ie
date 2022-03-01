from flask import request, Flask, jsonify
from flask_cors import CORS
from predict import *
import json

app = Flask(__name__)
# CORS(app, supports_credentials=True)
app.config['JSON_AS_ASCII'] = False


@app.route('/medical_ie', methods=['POST'])
def post_Data():
    # import json

    postdata = request.form['medical_content']
    if postdata:

        # 1.输入
        # (在生成输入文本的本地json文件，先清空一下的本地的历史生成文件)

        gene_path = "data/input/input_content.json"

        if os.path.exists(gene_path):
            os.remove(gene_path)


        dict1 = {"text": str(postdata)}
        with open(gene_path, "w", encoding="utf-8") as input_f:
            json.dump(dict1, input_f, ensure_ascii=False)

        # 2.
        #(在输出预测输出之前，先清空下本地的历史输出文件)
        output_path = r"output/test_predictions.json"

        if os.path.exists(output_path):
            os.remove(output_path)

        predict_re()

        with open(output_path, "r", encoding="utf-8") as ft:

            if json.load(ft)["spo_list"]:
                # 3.输出
                with open(output_path, 'r', encoding="utf-8") as output_f:
                    output_dict = json.load(output_f)

                recognize_info = {
                    "code": 200,
                    "msg": "success",
                    "data": output_dict,
                }
                return jsonify(recognize_info)
            else:
                recognize_info = {
                    "code": 404,
                    "msg": "当前没有识别出任何实体关系",
                    "data": {}
                }
                return jsonify(recognize_info)
    else:
        recognize_info = {
            "code": 400,
            "msg": "当前无输入数据，请重新输入",
            "data": {}
        }
        return jsonify(recognize_info)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
