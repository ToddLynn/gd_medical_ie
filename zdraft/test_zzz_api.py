from flask import Flask,jsonify
from flask_cors import CORS


"传字符串"
# app = Flask(__name__)
#
# @app.route('/fxxk')
# def fxxk():
#     return "golden states"
#
# app.run(port= 8080)



"传json"
app = Flask(__name__)
messages = [
    {
        "team":"China",
        "player" :[
    {
        "name":"yaoming",
        "number":11
    }
]
    }
]

#获取中国队的所有数据
@app.route('/messages')
def get_messages():
    return jsonify({"messages":messages})
app.config["JSON_AS_ASCII"] = False

CORS(app, resources=r'/*')

app.run(debug=False, host='0.0.0.0', port= 8080)