from sqlalchemy import Column, String, Integer

from app.db.base_class import Base


class Example(Base):
    __tablename__ = 'example'
    id = Column(Integer, primary_key=True)
    title = Column(String)
