# -*- coding: utf-8 -*-
# @Time    : 2024/11/26 14:40
# @Author  : Bytequestor
# @Site    : 
# @File    : flask_test_app.py
# @Software: PyCharm 
# @Comment : https://liaoxuefeng.com/books/python/web/web-framework/index.html
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>home</h1>'


@app.route('/sigin', methods=['GET'])
def sigin_form():
    return '''
        <form action="/sigin" method="post">
        <p><input name="username"></p>
        <p><input name="password" type="password"></p>
        <p><button type="submit">Sigin In</button></p>
        </form>
    '''


@app.route('/sigin', methods=['POST'])
def sigin():
    """
    在上一步的sigin_form中，提交了一个post请求，发送给/sigin，在此接到
    :return:
    """
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello,wzy!</h3>'
    return '<h3>Error</h3>'


if __name__ == '__main__':
    app.run()
