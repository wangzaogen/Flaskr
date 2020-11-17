from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager




# 初始化数据库连接:
engine = create_engine('mysql+pymysql://用户名:密码@数据库地址:3306/数据库名')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)



@contextmanager
def session_maker(session=DBSession):
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()