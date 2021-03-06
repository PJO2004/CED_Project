from API.db.database import Base
from sqlalchemy import Column, String, ForeignKey

'''
create table list
1. userdata
2. user_list
'''


class userdata(Base):
    __tablename__ = 'userdata'

    word = Column('word', String, primary_key=True)
    meaning = Column('meaning', String, unique=False)
    # foreign Key 보류
    # user = Column('user', String, ForeignKey("user_list.user"), unique=False)


class userlist(Base):
    __tablename__ = 'userlist'

    users_ = Column('users_', String, primary_key=True)
    passwd = Column('passwd', String, unique=False)
