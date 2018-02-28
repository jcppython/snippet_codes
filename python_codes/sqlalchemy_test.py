# -*- coding: utf-8 -*-

'''
文档: http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#version-check
TODO: Create a Schema
'''

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Sequence, Integer, String
from sqlalchemy.orm import sessionmaker, Session

# TODO: 暂时没搞明白
Base = declarative_base()

# class map to talbe [ORM Object Relational Mapper]
# 类对应一张表, 类对象对应表中一条记录
class User(Base):
    __tablename__ = 'users'
    id            = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name          = Column(String(50))
    fullname      = Column(String)
    password      = Column(String)

    # 非必要, 仅方便打印查看
    def __repr__(self):
        return "User(id=%s, name=%s, fullname=%s, password=%s)" % (
            self.id, self.name, self.fullname, self.password)

if __name__ == '__main__':
    print(sqlalchemy.__version__)
    # 1. engine 描述 database, session用户同数据库交互
    engine  = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)
    # TODO: sessionmaker与Session关系?
    session = sessionmaker(bind=engine)
    session = Session()


    # 2. 类实例代表一条记录
    # id将获得默认值'None'以应对AttributeError
    user1 = User(name='ed', fullname='Ed Jones', password='edspassword')
    print(user1)

    # 3. 用session与database交互
    session.add(user1)

    # query_user1 = session.query(User).filter_by(name='ed').first()
    # print(query_user1 is user1)


