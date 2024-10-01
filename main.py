from fastapi import FastAPI,Depends
import models
from database import engine
from router import member,staff,book,member_login,borrow_book
from middleware import get_api_key

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(member.router)
app.include_router(staff.router)
app.include_router(book.router)
app.include_router(member_login.router)
app.include_router(borrow_book.router)

# @app.get("/secure-endpoint")
# def secure_endpoint(api_key: str = Depends(get_api_key)):
#     return {"message": "Access granted", "api_key_provided": api_key}