from flask import Flask, request, render_template
from jinja2 import Template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# 动态路由
@app.route('/user/<name>')
def user(name):
    return '<h1> hello %s</h1>' % name

# url动态规则
@app.route('/item/<int:id>/')
def item(id):
    return 'Item: {}'.format(id)

# HTTP方法
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return 'POST'
    else:
        return 'GET'

# 渲染模板
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# 请求对象
# 响应
# 模板
template = Template('hello {{ name }}!')
print(template.render(name = 'candy'))


