from flask import Flask, render_template, request, json, jsonify, make_response

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # json属性配置


@app.route('/index')
def index():  # put application's code here
    data = {
        'name': '张三'
    }
    # return make_response(data)

    # return make_response(json.dumps(data,ensure_ascii = False))

    # response = make_response(json.dumps(data,ensure_ascii = False))
    # response.mimetype = 'application/json'
    # return response
    return jsonify(data)


if __name__ == '__main__':
    app.run()
