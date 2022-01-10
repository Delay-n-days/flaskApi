from flask import Flask, request
import json
import pock
app = Flask(__name__)
 
 
# 只接受POST方法访问
p = pock.poke()
p.DrawCards()
@app.route("/test_1",methods=["GET"])
def check():
    p.DrawCards()
    # 默认返回内容
    return_dict = {'statusCode': '200', 'message': 'successful!', 'result': {'user1':" ",'user2':" ",'user3':" ",'under':" "}}
    return_dict['result']['user1'] = p.PrintCard(p.user1Card)
    return_dict['result']['user2'] = p.PrintCard(p.user2Card)
    return_dict['result']['user3'] = p.PrintCard(p.user3Card)
    return_dict['result']['under'] = p.PrintCard(p.underCard)
    return json.dumps(return_dict, ensure_ascii=False)
 
@app.route("/xipai",methods=["GET"])
def xipai():
    p.DrawCards()
    # 默认返回内容
    return_dict = {'statusCode': '200', 'message': 'successful!', 'result': False}
    return_dict['result'] = True
    return json.dumps(return_dict, ensure_ascii=False)

@app.route("/user1",methods=["GET"])
def user1():
    # 默认返回内容
    return_dict = {'statusCode': '200', 'message': 'successful!', 'result': False}
    return_dict['result'] = p.PrintCard(p.user1Card)
    return json.dumps(return_dict, ensure_ascii=False)

@app.route("/user2",methods=["GET"])
def user2():
    # 默认返回内容
    return_dict = {'statusCode': '200', 'message': 'successful!', 'result': False}
    return_dict['result'] = p.PrintCard(p.user2Card)
    return json.dumps(return_dict, ensure_ascii=False)

@app.route("/user3",methods=["GET"])
def user3():
    # 默认返回内容
    return_dict = {'statusCode': '200', 'message': 'successful!', 'result': False}
    return_dict['result'] = p.PrintCard(p.user3Card)
    return json.dumps(return_dict, ensure_ascii=False)

@app.route("/under",methods=["GET"])
def under():
    # 默认返回内容
    return_dict = {'statusCode': '200', 'message': 'successful!', 'result': False}
    return_dict['result'] = p.PrintCard(p.underCard)
    return json.dumps(return_dict, ensure_ascii=False)

if __name__ == "__main__":
    app.run(debug=True,port=8083)
    p = pock.poke()
