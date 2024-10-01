from fastapi import Request,HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from starlette import status

class AuthenticationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        token = request.headers.get('Authorization')

        if not token:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Token not found")
        
        response = await call_next(request)
        return response
    
# app.add_middleware(AuthenticationMiddleware)
# this line is to be added in to make middleware work

# this piece of code is also not integrated with our App