from pydantic import BaseModel,Field
from datetime import date
from typing import Optional

class OurModelClass(BaseModel):
    class Config:
        from_attributes = True

class MemberCreate(OurModelClass):
    name: str
    email: str
    password: str  
    register_date: date

class User_data(OurModelClass):
    id:int
    name:str

class MemberShow(OurModelClass):
    id: int
    name: str
    email: str
    register_date: date

class StaffCreate(OurModelClass):
    name: str
    email: str
    password: str  

class StaffShow(OurModelClass):
    id: int
    name: str
    email: str

class Book(OurModelClass):
    name: str
    author: str
    genre:str
    count:int=Field(ge=0)
    pub_year:int


class BorrowedBook(OurModelClass):
    book_id: int
    member_id: int
    borrowed_date: Optional[date] = Field(default_factory=date.today)
    return_date: Optional[date] = None

class Credentials(OurModelClass):
    email: str
    password:str