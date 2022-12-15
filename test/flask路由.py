# 路由
from flask import Flask

app = Flask(__name__)


#直接访问网站就是GET请求 使用表单就是POST请求
@app.route('/hello', methods=['GET', 'POST'],endpoint='hello')  # 说明从网页匹配的路径是hello，匹配的请求是GET和POST,匹配的端点是hello
def hello():
    return 'helloworld'


@app.route('/hi'，methods = ['POST'])
def hi():
    return 'hi hi'


if __name__ == '__main__':
    app.run()
