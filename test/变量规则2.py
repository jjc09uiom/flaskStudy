from flask import Flask

app = Flask(__name__)


# int：接收正整数
# float：接收正浮点数
# path：接收包含斜杠的文本
# string:接收任何不包含斜杠的文本
@app.route('/user/<int:id>')  # 使用转换器定义不同的返回变量类型
def index(id):
    if id == 1:
        return 'python'
    if id == 2:
        return 'django'
    if id == 3:
        return 'flask'
    return 'hello world'


if __name__ == '__main__':
    app.run()
