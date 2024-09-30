from database import db
import models

class borrow_book_queries:
    def getBookById(book_id):
        return db.query(models.Book).filter(models.Book.id==book_id).first()
    
    def getBorrowedBook(book_id,member_id):
        return db.query(models.BorrowedBook).filter(
        models.BorrowedBook.member_id == member_id,
        models.BorrowedBook.book_id == book_id
    ).first()

    def add_borrow(borrow):
        db.add(borrow)
        db.commit()

    def refresh(fresh):
        db.refresh(fresh)
