
class Config:
    # 配置连接数据库的uri
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/covid"
    # 跟踪数据库数据的修改，然后自动更新模型类属性的值
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "hdsakm12546asdjhjakd4"