from flask import request, Flask, jsonify
from predict import *
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/medical_ie', methods=['POST'])
def post_Data():
    import json

    postdata = request.form['medical_content']
    if postdata:

        # 1.输入
        # 删除本地的json文件

        gene_path = "F:\workspace_dl_env\gd_medical_ie\data\input\kt_input1.json"

        if os.path.exists(gene_path):
            os.remove(gene_path)

        dict1 = {"text": str(postdata)}
        with open(gene_path, "w", encoding="utf-8") as input_f:
            json.dump(dict1, input_f, ensure_ascii=False)

        # 2.
        # 先删除一下
        output_path = r"F:\workspace_dl_env\gd_medical_ie\output\test_predictions.json"

        if os.path.exists(output_path):
            os.remove(output_path)

        predict_re()

        with open(output_path, "r", encoding="utf-8") as ft:

            if json.load(ft)["spo_list"]:
                # 3.输出
                with open(output_path, 'r', encoding="utf-8") as output_f:
                    output_dict = json.load(output_f)
                    # print(load_dict)

                recognize_info = {"result": output_dict}
                return jsonify(recognize_info), 201
                # todo 查询201
            else:
                return jsonify("没有识别出任何实体关系，请输入乳腺超声报告的相关文本")
    else:
        return jsonify("当前无数据，请重新输入")


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8888)
