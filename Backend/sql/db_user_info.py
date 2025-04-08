# framework
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
load_dotenv()

host=os.environ.get("SERVICE_DB_HOST", "localhost")
port=int(os.environ.get("LOCAL_DB_PORT", "5432"))
database=os.environ.get("SERVICE_DB", "postgres")
user=os.environ.get("SERVICE_DB_USER", "postgres")
password=os.environ.get("SERVICE_DB_PASSWORD", "postgres")

DB_URL = f"postgresql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(DB_URL)
Base = declarative_base()

class UserInfo(Base):
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(String(128), nullable=False)
    email = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)

# 세션 생성
Session = sessionmaker(bind=engine)
session = Session()

def _create_user_info(uid: str, email: str, password: str)->None:
    """
    # create userinfo
    """
    new_user = UserInfo(uid=uid, email=email, password=password)
    session.add(new_user)
    session.commit()
    session.close()

def _check_exist_user(email: str):
    existing_user = session.query(UserInfo).filter(UserInfo.email == email).first()
    session.close()
    return existing_user

def _check_duplicate_email(email: str):
    existing_user = _check_exist_user(email)
    if existing_user:
        return "fail"
    else:
        return "success"

def _check_exist_email(email: str):
    existing_user = _check_exist_user(email)
    if existing_user:
        return "success"
    else:
        return "fail"

def _check_user_info(email: str, password: str):
    try:
        user = session.query(UserInfo).filter(UserInfo.email == email, UserInfo.password == password).one()
        session.close()
        return {"uid": user.uid, "email": user.email}
    except:
        session.close()
        return "fail"