from sqlalchemy import Column, Integer, String, Float, ForeignKey

from app.db.base_class import Base


class Example(Base):
    __tablename__ = 'example'
    title = Column(String)
