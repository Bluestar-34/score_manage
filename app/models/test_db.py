# 在 Python 交互式环境中测试连接
import pymysql

try:
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='63663Yzd.',
        port=3306
    )
    print("MySQL 连接成功！")
    conn.close()
except Exception as e:
    print(f"MySQL 连接失败: {e}")