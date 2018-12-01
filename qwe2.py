import os
from source import crawling
from flask import Flask, request, jsonify
#from test import microdust_1


app = Flask(__name__)

#���ξ�����
@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type" : "buttons",
        "buttons":["��ȭ�ϱ�","����"]
    }
    return jsonify(dataSend)

@app.route('/message',methods = ['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    if content == u"��ȭ�ϱ�":
        dataSend = {
            "message":{
                "text" : "���Ӹ� ��ɾ� ��� \n1. ����\n2. �ȳ�\n3.����"
            }
        }
    elif content == u"����":
        dataSend = {
            "message" : {
                "text" : "�� ���Ӹ� �����մϴ�."
            }
        }
    elif u"�ȳ�" in content:
        dataSend = {
            "message" : {
                "text": "�ȳ��Ͻʴϱ�"
            }
        }
    elif u"����" in content:
        dataSend = {
            "message" : {
                "text" : "���� ���ž�"
            }
        }
    else:
        dataSend = {
            "message" : {
                "text" : content
            }
        }
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)