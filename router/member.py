from fastapi import APIRouter
from schemas import MemberCreate
from services.member_services import member_services

router = APIRouter()

@router.get('/get_member_by_id{member_id}')
async def get_member_by_id(member_id:int):
    return member_services.get_member_by_id(member_id)

@router.post('/create_member')
async def create_member(member:MemberCreate):
    return member_services.create_member(member)

@router.delete('/delete_member{member_id}')
async def delete_member(member_id:int):
    return member_services.delete_member(member_id)