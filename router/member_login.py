from fastapi import APIRouter,Depends
from services.login_services import login_services
from oauth2 import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post('/token')
async def login(form_data:OAuth2PasswordRequestForm=Depends()):
    user_details=login_services.authenticate_user(form_data)

    access_token = create_access_token(data={"user_id":user_details.id,"user_name":user_details.name})

    if user_details:
        return {"access_token":access_token,"token_type":"bearer"}



