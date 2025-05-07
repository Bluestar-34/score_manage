'''创建数据库模型'''

from datetime import datetime
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

print("开始加载数据库模型...")

class User(db.Model, UserMixin):
    """
    用户模型类
    继承自 db.Model 和 UserMixin
    - db.Model: SQLAlchemy 的模型基类，提供数据库操作功能
    - UserMixin: Flask-Login 的混入类，提供用户认证所需的方法
    """
    
    # 指定数据库表名
    __tablename__ = 'users'
    
    # 定义表字段
    id = db.Column(db.Integer, primary_key=True)  # 主键，自增整数
    username = db.Column(db.String(50), unique=True, nullable=False)  # 用户名，唯一且不能为空
    password_hash = db.Column(db.String(255), nullable=False)  # 密码哈希值，不能为空
    role = db.Column(db.Enum('admin', 'teacher'), nullable=False)  # 用户角色，只能是 admin 或 teacher
    last_login = db.Column(db.DateTime)  # 最后登录时间
    create_at = db.Column(db.DateTime, default=datetime.utcnow)  # 创建时间，默认为当前时间
    update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # 更新时间，自动更新

    def set_password(self, password):
        """
        设置用户密码
        参数:
            password: 原始密码
        功能:
            将原始密码加密后存储到 password_hash 字段
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        验证用户密码
        参数:
            password: 待验证的密码
        返回:
            bool: 密码是否正确
        """
        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        """
        检查用户是否是管理员
        返回:
            bool: 是否是管理员
        """
        return self.role == 'admin'

    def is_teacher(self):
        """
        检查用户是否是教师
        返回:
            bool: 是否是教师
        """
        return self.role == 'teacher'

print("User 模型已加载")

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.Enum('male', 'female'), nullable=False)
    class_name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

print("Student 模型已加载")

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(20), unique=True, nullable=False)
    course_name = db.Column(db.String(100), nullable=False)
    credit = db.Column(db.Numeric(3, 1), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

print("Course 模型已加载")

class Grade(db.Model):
    __tablename__ = 'grades'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), db.ForeignKey('students.student_id'), nullable=False)
    course_id = db.Column(db.String(20), db.ForeignKey('courses.course_code'), nullable=False)
    score = db.Column(db.Numeric(4,2), nullable=False)
    semester = db.Column(db.String(20), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint('student_id', 'course_id', 'semester', name='unique_grade'),
    )

print("Grade 模型已加载")
print("所有模型加载完成")