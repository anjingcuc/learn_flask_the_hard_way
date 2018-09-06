# -*- coding=utf8 -*-

# 从 flask 中导入一个可以用于实例化 WSGI app的类
from flask import Flask
# 实例化这个 WSGI 类
# ref: http://flask.pocoo.org/docs/latest/api/#flask.Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world.'

# __name__ 取值为 __main__ 说明当前py是程序的主入口
# 否则，说明当前py是以导入包的方式运行的
if __name__ == '__main__':
    app.run()

