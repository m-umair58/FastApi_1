from sqlalchemy import Column, Integer,String, ForeignKey, Date
from sqlalchemy.orm import relationship
from datetime import date
from database import Base


class BorrowedBook(Base):
    __tablename__ = 'borrowed_books'
    
    id = Column(Integer, primary_key=True, index=True)
    
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    
    member_id = Column(Integer, ForeignKey('members.id'), nullable=False)
    
    borrowed_date = Column(Date, nullable=False, default=date.today)
    
    return_date = Column(Date, nullable=True)

    book = relationship("Book", back_populates="borrowed_books")
    member = relationship("Member", back_populates="borrowed_books")


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    
    name=Column(String,nullable=False)

    author=Column(String,nullable=False)

    genre=Column(String,nullable=False)

    pub_year=Column(Integer,nullable=False)

    count = Column(Integer)

    borrowed_books = relationship("BorrowedBook", back_populates="book")

class Member(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True, index=True)
    
    name=Column(String,nullable=False)
    
    email=Column(String,nullable=False)
    
    password=Column(String,nullable=False)

    register_date=Column(Date,nullable=False, default=date.today)

    borrowed_books = relationship("BorrowedBook", back_populates="member")

class Staff(Base):
    __tablename__='staff'
    id = Column(Integer, primary_key=True, index=True)
    
    name=Column(String,nullable=False)
    
    email=Column(String,nullable=False)
    
    password=Column(String,nullable=False)
