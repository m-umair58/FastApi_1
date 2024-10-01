from fastapi import Request,HTTPException,Depends
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from starlette import status
from jose import jwt

from fastapi.security.api_key import APIKeyHeader
API_KEY_NAME = "Authorization"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key is None:
        raise HTTPException(
            status_code=403, detail="API key required"
        )
    return api_key



SECRET_KEY = "17b4ae5cbe59bf75d1a74dd7b5ec5d3f562606f492856b6eaf59e46916707765"
ALGORITHM = "HS256"

class AuthenticationMiddleware(BaseHTTPMiddleware):
    
    async def dispatch( request: Request,call_next) -> Response:
        token = request.headers.get('Authorization')
        if not token:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Token not found")

        if token.startswith("Bearer "):
            token = token[len("Bearer "):]
    
        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("user_name")
        userid: int = payload.get("user_id")
        
        if username is None or userid is None:
            raise HTTPException(status_code=401, detail="Unauthorized User")
        
        # return {"user_name": username, "id": userid}
    
        
        response = await call_next(request)
        return response
    
    # app.add_middleware(AuthenticationMiddleware)
    # this line is to be added in to make middleware work

    # this piece of code is also not integrated with our App

    # async def login_dispatch( request: Request) -> Response:
