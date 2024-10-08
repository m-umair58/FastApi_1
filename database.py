from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user='postgres'
password='admin'
port=5432
db_name='library'

DATABASE_URL = f'postgresql://{user}:{password}@localhost:{port}/{db_name}'

engine = create_engine(DATABASE_URL,echo=True)

SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()

db=SessionLocal()