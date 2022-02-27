from flask import request, Flask, jsonify
from predict import *
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/medical_ie', methods=['POST'])
def post_Data():
    import json

    postdata = request.form['medical_content']

    # 1.输入
    gene_path = "F:\workspace_dl_env\gd_medical_ie\data\input\kt_input1.json"
    dict1 = {"text": str(postdata)}
    with open(gene_path, "w", encoding="utf-8") as input_f:
        json.dump(dict1, input_f, ensure_ascii=False)

    # 2.
    predict_re()

    # 3.输出
    path1 = r"F:\workspace_dl_env\gd_medical_ie\output\test_predictions.json"
    with open(path1, 'r', encoding="utf-8") as output_f:
        output_dict = json.load(output_f)
        # print(load_dict)

    recognize_info = {"result": output_dict}
    return jsonify(recognize_info), 201


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8888)
