from db_queries.book_queries import book_queries
from schemas import Book
import models
from fastapi import HTTPException
from database import db

class book_services:
    def get_book_by_id(book_id:int):
        book_data=book_queries.getBookById(book_id)
        if book_data is None:
            raise HTTPException(status_code=404,detail=f"Member with id {book_id} not found")
        return book_data
    
    def add_book(book:Book):
        book_data=book_queries.getBookByName(book.name)
        if book_data:
            raise HTTPException(status_code=403,detail="Book Already exists")
        new_book=models.Book(**book.model_dump())# send what's inside the book
        book_queries.add_book(new_book)
        return {"message":"Book added successfully"}
    
    def delete_book(book_id:int):
        book_data=book_queries.getBookById(book_id)
        if book_data is None:
            raise HTTPException(status_code=404,detail=f"Member with id {book_id} is either already deleted or doesn't exists")
        
        book_queries.delete_book(book_data)

        return {"Message":"Book has been deleted successfully"}