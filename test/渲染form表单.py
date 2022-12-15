from flask import Flask, render_template

# render_template可以渲染表单页面
app = Flask(__name__, static_folder='./vue/dist/static', template_folder="./vue/dist")


# 设置静态文件夹目录

@app.route('/')
def index():
    return render_template('vue/index.html')


@app.route('/index', methods=['GET', 'POST'])
def index1():
    return render_template('test.html')


if __name__ == '__main__':
    app.run()
