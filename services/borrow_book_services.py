from db_queries.member_queries import member_queries
from db_queries.book_queries import book_queries
from db_queries.borrow_book_queries import borrow_book_queries
from fastapi import HTTPException
import models
from database import db
from datetime import date

class borrow_book_services:
    def borrow_book(member_id:int,book_id:int):
             
        book_data=book_queries.getBookById(book_id)
        if book_data is None:
            raise HTTPException(status_code=404,detail=f"Book with id {book_id} not found")
        if book_data.count==0:
             raise HTTPException(status_code=404,detail="Book is unavailable")
        memeber_data=member_queries.getMemberById(member_id)
        if memeber_data is None:
                raise HTTPException(status_code=404,detail=f"Member with id {member_id} not found")
        
        
        new_borrow=models.BorrowedBook(
            book_id=book_id,
            member_id=member_id
        )
        book_data.count-=1

        borrow_book_queries.add_borrow(new_borrow)
        borrow_book_queries.refresh(book_data)
        borrow_book_queries.refresh(new_borrow)
        

        return {"message":"Book Borrowed"}

    def return_book(member_id,book_id):
        memeber_data=member_queries.getMemberById(member_id)
        if memeber_data is None:
                raise HTTPException(status_code=404,detail=f"Member with id {member_id} not found")
        
        book_data=book_queries.getBookById(book_id)
        if book_data is None:
            raise HTTPException(status_code=404,detail=f"Book with id {book_id} not found")
        
        borrow_book_data=borrow_book_queries.getBorrowedBook(book_id,member_id)
        borrow_book_data.return_date=date.today()

        book_data.count+=1

        borrow_book_queries.commit()
        borrow_book_queries.refresh(book_data)
        borrow_book_queries.refresh(borrow_book_data)
        
        return {"message":f"Member with id {member_id} has returned the book with id {book_id}!"}

         
