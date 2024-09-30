from fastapi import FastAPI
import models
from database import engine
from router import member,staff,book,member_login,borrow_book

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(member.router)
app.include_router(staff.router)
app.include_router(book.router)
app.include_router(member_login.router)
app.include_router(borrow_book.router)