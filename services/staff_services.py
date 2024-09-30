from db_queries.staff_queries import staff_queries
from schemas import StaffCreate
import models
from fastapi import HTTPException
from database import db

class staff_services:
    def get_staff_by_id(staff_id:int):
        staff_data=staff_queries.getStaffById(staff_id)
        if staff_data is None:
            raise HTTPException(status_code=404,detail=f"Member with id {staff_id} not found")
        return staff_data
    
    def create_staff(staff:StaffCreate):
        staff_data=staff_queries.checkEmail(staff.email)
        if staff_data:
            raise HTTPException(status_code=403,detail="Email Already exists")
        new_staff=models.Staff(
            name=staff.name,
            email=staff.email,
            password=staff.password
        )
        db.add(new_staff)
        db.commit()

        return {"message":"Staff added successfully"}
    
    def delete_staff(staff_id:int):
        staff_data=staff_queries.getStaffById(staff_id)
        if staff_data is None:
            raise HTTPException(status_code=404,detail=f"Member with id {staff_id} is either already deleted or doesn't exists")
        
        db.delete(staff_data)
        db.commit()

        return {"Message":"Member has been deleted successfully"}