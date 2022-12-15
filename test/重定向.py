# 重定向 302状态
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/index')
def index():
    return redirect('https://www.baidu.com')  # 重定向到外部网页
    # redirect(url_for('hello')) 重定向到内部函数


@app.route('/')
def hello():
    return 'this is hello fun'


if __name__ == '__main__':
    app.run()
