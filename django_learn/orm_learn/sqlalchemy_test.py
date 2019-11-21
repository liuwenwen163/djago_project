# encoding: utf-8
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()  # 初始化模块
# 连接数据库引擎
engine = create_engine('mysql+pymysql:'
                       '//root:123456@localhost:3306/django_learn')
# 插入查询模块
db_session = sessionmaker(bind=engine)()


def init():
    """定义一个初始化数据库的方法"""
    Base.metadata.create_all(engine)


def drop():
    """定义一个删除数据库的方法"""
    Base.metadata.drop_all()


class User(Base):
    """定义一个User的数据模型"""
    __tablename__ = 'user' # 该名称等同于数据库中的表名

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    age = Column(Integer)


# if __name__ == '__main__':
#     """初始化创建数据库"""
#     init()

# # 一个完整的添加记录的过程
# user = User(name='liming', age=23)
# db_session.add(user)
# db_session.commit()
# db_session.close()

# 查找
user_one = db_session.query(User).filter_by(name='liming').one()
print(user_one)


