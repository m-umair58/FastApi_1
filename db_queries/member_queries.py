from database import db
import models

class member_queries:
    def getMemberById(member_id):
        return db.query(models.Member).filter(models.Member.id==member_id).first()
    
    def checkEmail(email):
        return db.query(models.Member).filter(models.Member.email==email).first()
    
    def checkPassword(password):
        return db.query(models.Member).filter(models.Member.password==password).first()
    
    def checkUsername(username):
        return db.query(models.Member).filter(models.Member.name==username).first()
    
    def add_member(member):
        db.add(member)
        db.commit()