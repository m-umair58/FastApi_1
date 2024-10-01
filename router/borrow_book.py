from fastapi import APIRouter,Depends
from services.borrow_book_services import borrow_book_services
from oauth2 import get_user_info
from schemas import User_data
from middleware import AuthenticationMiddleware


router = APIRouter()

@router.post('/borrow_book')
async def borrow_book(book_id,user_data:User_data=Depends(get_user_info)):#get_user_info is returning a dictionary
    return borrow_book_services.borrow_book(user_data['id'],book_id)# thats why we are using "user_data['id']""

@router.post('/return_book')
async def retrun_book(book_id,user_data:User_data=Depends(get_user_info)):
    return borrow_book_services.return_book(user_data['id'],book_id)
