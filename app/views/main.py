from flask import Blueprint, render_template
from flask_login import login_required, current_user

# 创建蓝图
main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
@login_required
def index():
    """主页面"""
    return render_template('index.html', title='首页') 