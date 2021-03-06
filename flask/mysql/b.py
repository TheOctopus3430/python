# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib import parse

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 't_user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
password = parse.quote_plus('yf3b@abc123')
# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:'+password+'@192.168.202.154:3303/spug')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()