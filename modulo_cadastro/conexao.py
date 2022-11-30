from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, create_engine

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:felipe008@localhost/login')
Session = sessionmaker()


class Usuario(Base):
    __tablename__ = 'tb_login9'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    usuario = Column(String(80), nullable=False, unique=True)
    senha = Column(String(40), nullable=False)


Base.metadata.create_all(engine)
