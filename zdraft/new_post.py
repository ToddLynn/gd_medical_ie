from flask import Flask,jsonify


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
app.run(port= 8080)