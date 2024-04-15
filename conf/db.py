from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


URI = "sqlite:///mydatabase.db"

engine = create_engine(URI)
DBSession = sessionmaker(bind=engine)
session = DBSession()