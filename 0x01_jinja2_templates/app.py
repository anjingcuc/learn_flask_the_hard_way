from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    # 调用内置的datetime.now函数获取当前时间。
    now_datetime = datetime.now()

    # 将datetime对象格式化为2017-01-01 12:12:12格式的日期字符串。
    now_string = now_datetime.strftime('%Y-%m-%d %H:%M:%S')

    # 调用flask库中的render_template函数渲染模板，并将now_string命名为变量now传给模板。
    return render_template('index.html', now=now_string)


if __name__ == '__main__':
    app.run()
