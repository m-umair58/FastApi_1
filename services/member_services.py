from db_queries.member_queries import member_queries
from schemas import MemberCreate
import models
from fastapi import HTTPException
from database import db
from passlib.context import CryptContext

bcrypt_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
def get_password_hash(password):
    return bcrypt_context.hash(password)

def verify_password(plain_password,hashed_password):
    return bcrypt_context.verify(plain_password,hashed_password)

class member_services:
    def get_member_by_id(member_id:int):
        member_data=member_queries.getMemberById(member_id)
        if member_data is None:
            raise HTTPException(status_code=404,detail=f"Member with id {member_id} not found")
        return member_data
    
    def create_member(member:MemberCreate):
        member_data=member_queries.checkEmail(member.email)
        if member_data:
            raise HTTPException(status_code=403,detail="Email Already exists")
        new_member=models.Member(
            name=member.name,
            email=member.email,
            password=get_password_hash(member.password)
        )
        db.add(new_member)
        db.commit()

        return {"message":"Member added successfully"}
    
    def delete_member(member_id:int):
        member_data=member_queries.getMemberById(member_id)
        if member_data is None:
            raise HTTPException(status_code=404,detail=f"Member with id {member_id} is either already deleted or doesn't exists")
        
        db.delete(member_data)
        db.commit()

        return {"Message":"Member has been deleted successfully"}