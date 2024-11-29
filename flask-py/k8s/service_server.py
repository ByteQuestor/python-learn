#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：flask-py 
@File    ：service_server.py
@Author  ：【闲鱼】：混吃等死真君
@Date    ：2024/11/29 10:32 
'''
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def submit_data():
    # 获取请求体中的 JSON 数据
    data = request.get_json()
    return f"{data['name']}.yaml"


@app.route("/delete/<id>", methods=['DELETE'])
def delete_svc(id):
    num = id
    print(num)
    return {"delete success": num}


app.run(host='0.0.0.0', port=8888)
