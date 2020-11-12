from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, String, create_engine
from sqlalchemy.orm import sessionmaker
import Parser

engine = create_engine('mysql://root:@localhost/test?charset=utf8', convert_unicode=False)
Session = sessionmaker()
Base = declarative_base()
session = Session(bind=engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(INTEGER, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)


def __repf__(self):
    return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                   self.name, self.fullname, self.nickname)


def insert(NAME, FULLNAME, NICKNAME):
    ed_user = User(name=NAME, fullname=FULLNAME, nickname=NICKNAME)
    session.add(ed_user)
    session.commit()
