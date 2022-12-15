# 模板 jinja2

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index')
def index():
    data = {
        'name': '张三',
        'age': 18,
        'mylist': [1, 2, 3, 4, 5, 6]
    }
    return render_template('index2.html', data=data)


def list_step(li):
    """自定义过滤器"""
    return li[::2]


# 注册过滤器 1.自定义函数的名字 2.前端用到时的名字
app.add_template_filter(list_step, 'li2')

# li = [1, 2, 3, 4, 5]

# print(list_step(li))

if __name__ == '__main__':
    app.run()
