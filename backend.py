import sqlite3
from venv import create


def connect():
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()



def insert(title,author,year,isbn):
    if title and author and year and isbn:
        conn = sqlite3.connect('books.db')
        curr = conn.cursor()
        curr.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        conn.commit()
        conn.close()
        return True
    else:
        return False

def view():
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()
    curr.execute("SELECT * FROM book")
    rows = curr.fetchall()
    conn.close()
    return rows


def search(title,author,year,isbn):
    if title or author or year or isbn:
        conn = sqlite3.connect('books.db')
        curr = conn.cursor()
        curr.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows = curr.fetchall()
        conn.close()
        return rows
    else:
        return []

def delete(id):
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()
    curr.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()
 
def update(id,title,author,year,isbn):
    if title and author and year and isbn:
        conn = sqlite3.connect('books.db')
        curr = conn.cursor()
        curr.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        conn.commit()
        conn.close()
        return True
    else:
        return False

 

connect()
