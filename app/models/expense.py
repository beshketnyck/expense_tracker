from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    comment = Column(String(200), nullable=True)
    date = Column(String, nullable=False)