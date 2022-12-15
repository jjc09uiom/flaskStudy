# flask数据库
# pip install flask-sqlslchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)


class Config:
    '''配置参数'''

    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)

# SQLAlchemy 和app 绑定
db = SQLAlchemy(app)


# 创建数据库模型类
class Role(db.Model):
    '''角色表'''
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)


class User(db.Model):
    '''用户表'''
    __tablename__ = 'user'

    id = db.Column(db.Integer, Primary_key=True)  # 默认设置自增长
    name = db.Column(db.String(128), unique=True)
    password = db.Column(db.STring(128))
    # 表关系 外键ForeignKey 用来关联到另一张表
    role_id = db.Column(db.Integer, ForeignKey('role_id'))

    def __repr__(self):
        return '%s' % self.name


if __name__ == '__main__':
    # 清除所有表
    db.drop_all()
    # 创建所有表
    db.create_all()

    # 创建对象 插入数据
    role1 = Role(name='admin')
    # session记录到对象任务中
    db.session.add(role1)
    # 提交任务
    db.session.commit()
