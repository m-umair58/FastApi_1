from fastapi import APIRouter
from schemas import StaffCreate
from services.staff_services import staff_services

router = APIRouter()

@router.get('/get_staff_by_id{staff_id}')
async def get_staff_by_id(staff_id:int):
    return staff_services.get_staff_by_id(staff_id)

@router.post('/create_staff')
async def create_staff(staff:StaffCreate):
    return staff_services.create_staff(staff)

@router.delete('/delete_staff{staff_id}')
async def delete_staff(staff_id:int):
    return staff_services.delete_staff(staff_id)