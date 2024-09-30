from database import db
import models

class book_queries:
    def getBookById(book_id):
        return db.query(models.Book).filter(models.Book.id==book_id).first()
    
    def getBookByName(name):
        return db.query(models.Book).filter(models.Book.name==name).first()
    
    def add_book(book):
        db.add(book)
        db.commit()

    def delete_book(book):
        db.delete(book)
        db.commit()
