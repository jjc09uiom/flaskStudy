# request 包含前端发送过来的所有请求
from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/test',methods=['GET','POST'])
def test():
    if request.method == 'GET':
        return render_template('test2.html')
    if request.method == 'POST':
        name = request.form.get('name') # 从request对象得到前端form表单的数据
        password = request.form.get('password')
        print(name,password)
        return 'this is post'


if __name__ == '__main__':
    app.run()
