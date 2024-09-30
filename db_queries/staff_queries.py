from database import db
import models

class staff_queries:
    def getStaffById(staff_id):
        return db.query(models.Staff).filter(models.Staff.id==staff_id).first()
    
    def checkEmail(email):
        return db.query(models.Staff).filter(models.Staff.email==email).first()
    
    def add_staff(staff):
        db.add(staff)
        db.commit()

    def delete_staff(staff):
        db.delete(staff)
        db.commit()
