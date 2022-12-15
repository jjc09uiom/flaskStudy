from flask import Flask

app = Flask(__name__)


@app.route('/user/<id>')  # 在route中接收前端url的不同变量
def index(id):  # 监控号默认以字符的形式返回
    if id == '1':   # index接受id变量后在函数中定义不同的分支匹配变量
        return 'python'
    if id == str(2):
        return 'django'
    if int(id) == 3:
        return 'flask'
    return 'hello world'


if __name__ == '__main__':
    app.run()
