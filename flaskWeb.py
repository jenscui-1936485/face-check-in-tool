#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask,request,render_template, redirect,url_for
from lib.manage import Manage

app = Flask(__name__)

@app.route('/test')
def test():
    return render_template('upload.html')

@app.route("/upload", methods = ['POST'])
def upload():
    if request.method == 'POST':
        name = request.form["Name"]
        user_id = request.form['ID']
        email = request.form['Email']

        #添加照片到人脸库
        register = Manage(user_id, name, email, user_id)
        register.Create()

        return {
            "code": 0,   #表示成功
            "data" : "success"
        }

@app.route("/test2")
def test2():
    return render_template('query.html')

@app.route("/query", methods = ['POST'])
def query():
    if request.method == 'POST':

        register = Manage('test', 'test', 'test', 'test')
        register.Query()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
