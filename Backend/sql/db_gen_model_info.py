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

class GenModelInfo(Base):
    __tablename__ = 'gen_model_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    g_model_name = Column(String(256), nullable=False)

# 세션 생성
Session = sessionmaker(bind=engine)
session = Session()

def _check_exist_gen_model(g_model_name):
    existing_model = session.query(GenModelInfo).filter(
        GenModelInfo.g_model_name == g_model_name
    ).first()
    session.close()
    if existing_model:
        return "fail"
    else:
        return "success"

def _insert_gen_model_info(g_model_name)->None:
    gen_model_info = GenModelInfo(g_model_name=g_model_name)
    session.add(gen_model_info)
    session.commit()
    session.close()

def _search_gen_model_info():
    gen_model_info = session.query(GenModelInfo).all()
    session.close()
    response = [i.g_model_name for i in gen_model_info]
    return response