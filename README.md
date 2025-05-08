# 学生成绩管理系统

一个基于 Flask 和 MySQL 的 Web 应用程序，用于管理学生信息和成绩。

## 功能特点

- 用户认证系统（登录/注册）
- 角色权限管理（管理员/教师）
- 学生信息管理
- 课程管理
- 成绩管理
- 数据统计和可视化

## 技术栈

- **后端框架**: Flask
- **数据库**: MySQL
- **ORM**: SQLAlchemy
- **前端框架**: Bootstrap
- **模板引擎**: Jinja2
- **用户认证**: Flask-Login
- **表单处理**: Flask-WTF

## 项目结构

```
student_management/
├── app/                    # 应用主目录
│   ├── __init__.py        # 应用工厂
│   ├── config.py          # 配置文件
│   ├── models/            # 数据模型
│   │   ├── __init__.py
│   │   └── models.py
│   ├── forms/             # 表单类
│   │   ├── __init__.py
│   │   └── forms.py
│   ├── views/             # 视图函数
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── main.py
│   └── templates/         # HTML 模板
│       ├── base.html
│       ├── auth/
│       │   ├── login.html
│       │   └── register.html
│       └── index.html
├── venv/                  # 虚拟环境
├── requirements.txt       # 项目依赖
├── create_test_user.py    # 测试用户创建脚本
└── README.md             # 项目说明文档
```

## 安装说明

1. **克隆项目**
   ```bash
   git clone [项目地址]
   cd student_management
   ```

2. **创建虚拟环境**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **配置数据库**
   - 创建 MySQL 数据库
   - 修改 `app/config.py` 中的数据库配置
   ```python
   SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/dbname"
   ```

5. **初始化数据库**
   ```bash
   python init_db.py
   ```

6. **创建测试用户**
   ```bash
   python create_test_user.py
   ```

## 运行应用

```bash
flask run
```

访问 http://localhost:5000 即可使用系统。

## 使用说明

### 用户角色

1. **管理员**
   - 管理所有用户
   - 查看所有数据
   - 系统配置

2. **教师**
   - 管理学生信息
   - 录入和修改成绩
   - 查看统计数据

### 主要功能

1. **用户管理**
   - 用户注册
   - 用户登录
   - 密码修改

2. **学生管理**
   - 添加学生信息
   - 修改学生信息
   - 查询学生信息

3. **课程管理**
   - 添加课程
   - 修改课程信息
   - 课程查询

4. **成绩管理**
   - 录入成绩
   - 修改成绩
   - 成绩查询
   - 成绩统计

## 开发说明

### 添加新功能

1. 在 `app/models/` 中添加新的数据模型
2. 在 `app/forms/` 中创建相应的表单类
3. 在 `app/views/` 中实现视图函数
4. 在 `app/templates/` 中创建模板文件

### 代码规范

- 遵循 PEP 8 编码规范
- 使用英文命名变量和函数
- 添加适当的注释和文档字符串
- 保持代码简洁和可维护性

## 测试

### 单元测试
```bash
python -m pytest tests/
```

### 功能测试
1. 用户注册和登录
2. 学生信息管理
3. 成绩录入和查询
4. 数据统计功能

## 部署

### 生产环境配置
1. 修改 `config.py` 中的配置
2. 设置环境变量
3. 使用生产级 WSGI 服务器（如 Gunicorn）
4. 配置 Nginx 反向代理

### 安全建议
1. 使用 HTTPS
2. 定期更新依赖包
3. 实施访问控制
4. 数据定期备份

## 贡献指南

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

MIT License

## 联系方式

如有问题或建议，请提交 Issue 或联系项目维护者。 