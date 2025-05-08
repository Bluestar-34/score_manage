'''表单类定义模块
该模块包含两个主要的表单类：
1. LoginForm - 处理用户登录
2. RegisterForm - 处理用户注册
'''

from flask_wtf import FlaskForm  # Flask-WTF 表单基类
from wtforms import StringField, PasswordField, SubmitField, SelectField, ValidationError  # 表单字段类型
from wtforms.validators import DataRequired, EqualTo, Email, Length  # 表单验证器
from app.models.models import User  # 导入用户模型

class LoginForm(FlaskForm):
    """登录表单类
    
    属性:
        username: 用户名字段，必填，长度3-20字符
        password: 密码字段，必填，最少6字符
        submit: 提交按钮
    """
    # 用户名字段定义
    username = StringField('用户名', validators=[
        DataRequired(message='请输入用户名'),  # 必填验证
        Length(min=3, max=20, message='用户名长度必须在3-20个字符之间')  # 长度验证
    ])
    
    # 密码字段定义
    password = PasswordField('密码', validators=[
        DataRequired(message='请输入密码'),  # 必填验证
        Length(min=6, message='密码长度不能少于6个字符')  # 长度验证
    ])
    
    # 提交按钮
    submit = SubmitField('登录')

class RegisterForm(FlaskForm):
    """注册表单类
    
    属性:
        username: 用户名字段，必填，长度3-20字符
        password: 密码字段，必填，最少6字符
        confirm_password: 确认密码字段，必须与密码字段相同
        role: 角色选择字段，必填
        submit: 提交按钮
    """
    # 用户名字段定义
    username = StringField('用户名', validators=[
        DataRequired(message='请输入用户名'),  # 必填验证
        Length(min=3, max=20, message='用户名长度必须在3-20个字符之间')  # 长度验证
    ])

    # 密码字段定义
    password = PasswordField('密码', validators=[
        DataRequired(message='请输入密码'),  # 必填验证
        Length(min=6, message='密码长度不能少于6个字符')  # 长度验证
    ])

    # 确认密码字段定义
    confirm_password = PasswordField('确认密码', validators=[
        DataRequired(message='请确认密码'),  # 必填验证
        EqualTo('password', message='两次输入的密码不一致')  # 确保与密码字段相同
    ])

    # 角色选择字段定义
    role = SelectField('角色', choices=[
        ('admin', '管理员'),  # 管理员选项
        ('teacher', '教师')   # 教师选项
    ], validators=[DataRequired(message='请选择角色')])  # 必填验证

    # 提交按钮
    submit = SubmitField('注册')

    def validate_username(self, field):
        """自定义验证方法：检查用户名是否已存在
        
        参数:
            field: 用户名字段对象
            
        异常:
            ValidationError: 当用户名已存在时抛出
        """
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名已被使用')