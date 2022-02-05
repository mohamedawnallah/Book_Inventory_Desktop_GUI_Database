import sqlite3
from venv import create

class Database:

    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.curr = self.conn.cursor()
        self.curr.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def insert(self,title,author,year,isbn):
        if title and author and year and isbn:
            self.curr.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
            self.conn.commit()
            return True
        else:
            return False

    def view(self):
        self.curr.execute("SELECT * FROM book")
        rows = self.curr.fetchall()
        return rows


    def search(self,title,author,year,isbn):
        if title or author or year or isbn:
            self.curr.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
            rows = self.curr.fetchall()
            return rows
        else:
            return []

    def delete(self,id):
        self.curr.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()
    
    def update(self,id,title,author,year,isbn):
        if title and author and year and isbn:
            self.curr.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
            self.conn.commit()
            return True
        else:
            return False

    def __del__(self):
        self.conn.close()

    

