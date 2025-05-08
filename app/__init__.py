# 导入必要的模块
from flask import Flask  # 导入 Flask 框架
from flask_sqlalchemy import SQLAlchemy  # 导入 SQLAlchemy 数据库 ORM
from flask_login import LoginManager
from .config import Config  # 导入配置文件

# 创建数据库实例
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    """
    创建并配置 Flask 应用
    这是一个工厂函数，用于创建 Flask 应用实例
    返回: Flask 应用实例
    """
    # 创建 Flask 应用实例
    app = Flask(__name__)
    
    # 从配置文件加载配置
    # config 对象包含数据库连接信息等配置
    app.config.from_object(Config)

    # 初始化数据库
    # 将 Flask 应用实例与 SQLAlchemy 绑定
    db.init_app(app)    
    login_manager.init_app(app)

    # 导入模型以确保它们被注册
    from .models.models import User, Student, Course, Grade
    print("模型已导入到应用中")
    '''
    入模型以确保它们被注册
    from .models.models import User, Student, Course, Grade
    print("模型已导入到应用中")'''

    #设置登录视图
    login_manager.login_view = 'auth.login'
    login_manager.login_message = '请先登录'
    login_manager.login_message_category = 'info'

    #注册蓝图
    from .views.auth import auth
    from .views.main import main
    app.register_blueprint(auth)
    app.register_blueprint(main)
    
    # 返回配置好的 Flask 应用实例
    return app

@login_manager.user_loader
def load_user(user_id):
    from .models.models import User
    return User.query.get(int(user_id))
