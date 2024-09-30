from db_queries.member_queries import member_queries
from fastapi import HTTPException
from schemas import User_data

class login_services:
    def authenticate_user(credentials):
        user_details=member_queries.checkUsername(credentials.username)

        if user_details is None:
            raise HTTPException(status_code=404,detail="Email is Incorrect")
        
        if user_details.password!=credentials.password:
            raise HTTPException(status_code=404,detail="Password is Incorrect")
        
        user_show=User_data(
            id=user_details.id,
            name=user_details.name
        )
        return user_show

