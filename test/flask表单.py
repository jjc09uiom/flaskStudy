import token

from flask import Flask, render_template, request
from wtforms import StringField, PasswordField, SubmitField  # 类型
from flask_wtf import FlaskForm, csrf
from wtforms.validators import DataRequired, EqualTo  # 验证数据不能为空 验证数据是否相同

app = Flask(__name__)

app.config['SECRET_KEY'] = 'AHNAHSJAH'


# 定义表单模型类
class Register(FlaskForm):
    user_name = StringField(label='用户名', validators=[DataRequired('用户名不能为空')])
    password = PasswordField(label='密码', validators=[DataRequired('密码不能为空')])
    password2 = PasswordField(label='再次输入密码', validators=[DataRequired('密码不能为空'), EqualTo('password')])
    submit = SubmitField(label='提交')


@app.route('/register', methods=['GET', 'POST'])
def register():
    # 创建表单对象
    form = Register()
    if request.method == 'GET':
        return render_template('register.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            # validate_on_submit 验证器 表单传过来的数据如果都是正确的就会继续往后执行
            '''
            必须html文件的form标签下添加{{ form.hidden_tag() }}才能使用正确判断
            '''
            username = form.user_name.data
            password = form.password.data
            password2 = form.password2.data
            print(username)
            print(password)
            print(password2)
        else:
            print('验证失败')
        return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run()
