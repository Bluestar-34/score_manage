'''测试用户创建脚本
该脚本用于创建测试用户，主要用于开发和测试环境。
创建的用户信息：
- 用户名: test
- 密码: test123
- 角色: student
'''

from app import create_app, db  # 导入应用工厂和数据库实例
from app.models.models import User  # 导入用户模型

def create_test_user():
    """创建测试用户函数
    
    功能：
    1. 创建应用上下文
    2. 检查测试用户是否已存在
    3. 如果不存在，创建新用户
    4. 如果已存在，提示用户已存在
    
    注意：
    - 该函数应在应用上下文中运行
    - 用户密码会被自动加密存储
    """
    app = create_app()  # 创建应用实例
    with app.app_context():  # 创建应用上下文
        # 检查用户是否已存在
        user = User.query.filter_by(username='test').first()
        if not user:
            # 创建新用户
            user = User(
                username='test',  # 设置用户名
                role='teacher'    # 设置角色为老师
            )
            user.set_password('test123')  # 设置密码（会自动加密）
            db.session.add(user)  # 添加到数据库会话
            db.session.commit()   # 提交更改
            print('测试用户创建成功！')
        else:
            print('测试用户已存在！')

if __name__ == '__main__':
    create_test_user()  # 运行测试用户创建函数 