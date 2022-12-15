# <>提取参数
# <int:id> int转换器

# 自定义转换器
from werkzeug.routing import BaseConverter
from flask import Flask

app = Flask(__name__)


class RegexConverter(BaseConverter):
    # 自定义转换器类
    def __init__(self, url_map, regex):
        # 调用父类的方法
        super(RegexConverter, self).__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        # 父类的方法，功能已经实现好了
        print("to_python方法被调用")
        return value


# 将自定义的转换器添加到flask应用中
app.url_map.converters['re'] = RegexConverter


@app.route('/index/<re("123"):value>')  # 1\d{10}   以1开头的十位数字
def index(value):
    print(value)
    return 'hello'


if __name__ == '__main__':
    app.run()
