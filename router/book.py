from fastapi import APIRouter
from schemas import Book
from services.book_services import book_services

router = APIRouter()

@router.get('/get_book_by_id{book_id}')
async def get_book_by_id(book_id:int):
    return book_services.get_book_by_id(book_id)

@router.post('/add_book')
async def add_book(book:Book):
    return book_services.add_book(book)

@router.delete('/delete_book{book_id}')
async def delete_book(book_id:int):
    return book_services.delete_book(book_id)