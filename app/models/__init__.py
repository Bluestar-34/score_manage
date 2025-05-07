# 导入必要的模块
from app import create_app, db  # 导入数据库实例，用于数据库操作
import pymysql  # 导入 PyMySQL，用于直接操作 MySQL 数据库
from app.config import Config  # 导入配置类，包含数据库连接信息



class DBinfo():

    def __init__(self):
        db_uri = Config.SQLALCHEMY_DATABASE_URI
        # 解析数据库连接信息
        # 格式：mysql+pymysql://username:password@host/dbname
        db_info = db_uri.split('://')[1]  # 获取 username:password@host/dbname 部分
        user_pass, host_db = db_info.split('@')  # 分离用户信息和主机信息
        self.username, self.password = user_pass.split(':')  # 分离用户名和密码
        host_port, self.dbname = host_db.split('/')  # 分离主机地址和数据库名
        self.host = host_port.split(':')[0]
        self.port = host_port.split(':')[1]

db_info = DBinfo()
username, password, host, dbname = db_info.username, db_info.password, db_info.host, db_info.dbname
print(username, password, host, dbname)

def create_db():
    """
    创建数据库函数
    功能：根据配置信息创建 MySQL 数据库
    步骤：
    1. 解析数据库连接字符串
    2. 建立数据库连接
    3. 创建数据库
    4. 关闭连接
    """

    
    # 从配置中获取数据库连接 URI

    try:
        # 创建数据库连接
        # 注意：这里不指定数据库名，因为数据库可能还不存在
        conn = pymysql.connect(
            host= host,  # 数据库主机地址
            user= username,  # 数据库用户名
            password= password  # 数据库密码
        )

        # 创建游标对象，用于执行 SQL 命令
        cursor = conn.cursor()

        # 执行创建数据库的 SQL 命令
        # IF NOT EXISTS 确保如果数据库已存在则不会报错
        cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(dbname))
        print("数据库创建成功")  # 打印成功信息

        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        conn.close()

    except Exception as e:
        # 异常处理
        # 如果创建过程中出现任何错误，打印错误信息
        print(f"数据库创建失败: {e}")

        

def check_mysql_connection():
    """
    检查 MySQL 连接是否成功
    功能：检查 MySQL 数据库连接是否成功
    步骤：
    1. 解析数据库连接信息
    """
    try:
        conn = pymysql.connect(
            host= host,
            user= username,
            password= password
        )
        print("MySQL 连接成功")
        conn.close()
        return True
    except Exception as e:
        print(f"MySQL 连接失败: {e}")
        return False
        

def init_db():
    """
    初始化数据库函数
    用于创建所有数据库表
    使用应用上下文确保数据库操作在正确的环境中执行
    """

    if not check_mysql_connection():
        print("MySQL 连接失败，无法初始化数据库")
        return

    try:
        # 创建 Flask 应用实例
        create_db()
        
        # 使用应用上下文
        # 应用上下文提供了应用运行时的环境
    # 确保数据库操作在正确的应用环境中执行
        app = create_app()
        with app.app_context():
            # 创建所有数据库表
            # 根据模型定义创建对应的数据库表
            # 如果表已存在，则不会重复创建
            db.create_all()
            #db.create_all() 在表已存在时 ​​不会重复创建​​，也不会覆盖已有表。这是 SQLAlchemy 的 ​​安全设计机制
            # 打印成功信息
            print("数据库表创建成功！")
    except Exception as e:
        print(f"数据库表创建失败: {e}")
        raise

# 当直接运行此脚本时执行
if __name__ == '__main__':
    # 调用初始化数据库函数
    init_db()

    

