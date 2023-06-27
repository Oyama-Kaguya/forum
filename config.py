from datetime import timedelta

db_conn_config = {
    'dialect': 'mysql',
    'driver': 'pymysql',
    'username': 'forum_develop',
    'password': 'forum_develop',
    'host': 'localhost',
    'port': '3306',
    'database': 'forum_test'
}


# 配置环境的基类
class Config(object):
    # 每次请求结束后，自动提交数据库中的变动，该字段在flask-sqlalchemy 2.0之后已经被删除了（有bug）
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # 2.0之后新加字段，flask-sqlalchemy 将会追踪对象的修改并且发送信号。
    # 这需要额外的内存，如果不必要的可以禁用它。
    # 注意，如果不手动赋值，可能在服务器控制台出现警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 数据库操作时是否显示原始SQL语句，一般都是打开的，因为后台要日志
    SQLALCHEMY_ECHO = True


# 开发环境的配置
class DevelopmentConfig(Config):
    """
    配置文件中的所有的账号密码等敏感信息，应该避免出现在代码中，可以采用从环境变量中引用的方式，比如：
    username = os.environ.get('MYSQL_USER_NAME')
    password = os.environ.get('MYSQL_USER_PASSWORD')
    本文为了便于理解，将用户信息直接写入了代码里
    """
    DEBUG = True
    JWT_SECRET_KEY = '123456789abcdefg'
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=10)
    # 数据库URI
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:xxx@xxxx/xxx'

    # 也可如下来写，比较清晰
    SQLALCHEMY_DATABASE_URI = "{dialect}+{driver}://{username}:{password}@{host}:{port}" \
                              "/{database}?charset=utf8mb4".format(**db_conn_config)


# 测试环境的配置
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@172.17.180.3:3306/test'

    """
    测试环境也可以使用sqlite，默认指定为一个内存中的数据库，因为测试运行结束后无需保留任何数据
    也可使用  'sqlite://' + os.path.join(basedir, 'data.sqlite') ，指定完整默认数据库路径
    """
    # import os
    # basedir = os.path.abspath(os.path.dirname(__file__))
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'


# 生产环境的配置
class ProductionConfig(Config):
    pass
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:xxx@xxxx:3306/xxxx'


# 初始化app实例时对应的开发环境声明
configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
