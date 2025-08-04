from symtable import Class

from datetime import datetime

import psycopg2
from prettytable import PrettyTable

conn = psycopg2.connect(
dbname = 'dorixona',
user = "postgres",
password = "911508Ff",
port=5432,
host='localhost'
)
curr = conn.cursor()


# curr.execute(f"create table users(id serial primary key,"
#              f"full_name VARCHAR(100),"
#              f"email VARCHAR(100),"
#              f"password TEXT,"
#              f"created_at TIMESTAMP)")

# curr.execute(f"create table books(id serial primary key,"
#              f"title VARCHAR(100),"
#              f"author_id INT,"
#              f"description TEXT,"
#              f"published_year INT,"
#              f"genre_id INT,"
#              f"created_at TIMESTAMP,"
#              f"foreign key (author_id) references authors(id),"
#              f"foreign key (genre_id) references genres(id))")

# curr.execute(f"create table authors(id serial primary key,"
#              f"full_name VARCHAR(100),"
#              f"country VARCHAR(100))")
#
# curr.execute(f"create table genres(id serial primary key,"
#              f"name VARCHAR(50))")
#
# curr.execute(f"create table comments(id serial primary key,"
#              f"user_id INT,"
#              f"book_id INT,"
#              f"content TEXT,"
#              f"reated_at TIMESTAMP,"
#              f"foreign key (user_id) references users(id),"
#              f"foreign key (book_id) references books(id))")
# conn.commit()
# conn.close()


class Users:
    def __init__(self, full_name, email, password, created_at):
        self.full_name = full_name
        self.email = email
        self.password = password
        self.created_at = created_at

    def registered(self):
        curr.execute(f"select *from users where full_name = '{self.full_name}'")
        top = curr.fetchone()
        if top:
            print("Siz Ro'yhatdan o'tgansiz")
        else:
            curr.execute(f"insert into users (full_name, email, password, created_at) values ("
                         f"{self.full_name}, {self.email}, {self.password}, {self.created_at}))")
            conn.commit()
            print("Siz ro'yhatdan o'tdingiz")


class Book:
    def __init__(self, title, author_id, description, published_year, genre_id, created_at):
        self.title = title
        self.author_id = author_id
        self.description = description
        self.published_year = published_year
        self.genre_id = genre_id
        self.created_at = created_at

    def qoshish(self):
        curr.execute(f"""
            INSERT INTO books (title, author_id, description, published_year, genre_id, created_at)
            VALUES ({self.title}, {self.author_id}, {self.description}, {self.published_year}, {self.genre_id}, {self.created_at})
        """)
        conn.commit()
        print("Kitob qo‘shildi!!")

    def update(self, new_description):
        curr.execute(f"""
            UPDATE books SET title = {self.title}, published_year = {self.description}
            WHERE description = {new_description}
        """)
        conn.commit()
        print("Kitob yangilandi")

    def delete(self, book_id):
        curr.execute(f"DELETE FROM books WHERE id = {book_id}")
        conn.commit()
        print("Kitob o‘chdi")

class Comment:
    def __init__(self, user_id, book_id, content, reated_at):
        self.user_id = user_id
        self.book_id = book_id
        self.content = content
        self.reated_at = reated_at

    def add(self):
        curr.execute(f"""
            INSERT INTO comments (user_id, book_id, content, reated_at)
            VALUES ({self.user_id}, {self.book_id}, {self.content}, {self.reated_at})
        """)
        conn.commit()
        print("Izoh qo‘shildi")

    def update(self, comment_id, new_comments):
        curr.execute(f"""
            UPDATE comments SET content = {new_comments}, reated_at = {self.reated_at} WHERE id = {comment_id}
        """)
        conn.commit()
        print("Izoh tahrirlandi")

    def delete(self, comment_id):
        curr.execute(f"DELETE FROM comments WHERE id = {comment_id}")
        conn.commit()
        print("Izoh o‘chirildi")

class Author:
    def __init__(self, full_name, country):
        self.full_name = full_name
        self.country = country

    def add(self):
        curr.execute(f"INSERT INTO authors (full_name, country) VALUES ({self.full_name}, {self.country})")
        conn.commit()
        print("Muallif qo‘shildi!!")


class Genre:
    def __init__(self, name):
        self.name = name

    def add(self):
        curr.execute(f"INSERT INTO genres (name) VALUES ({self.name})")
        conn.commit()
        print("Janr qo‘shildi")

    def update(self, genre_id):
        curr.execute(f"UPDATE genres SET name = {self.name} WHERE id = {genre_id}")
        conn.commit()
        print("Janr yangilandi")

    def delete(self, genre_id):
        curr.execute(f"DELETE FROM genres WHERE id = {genre_id}")
        conn.commit()
        print("Janr o‘chirildi")


# users_data = [
#     ("Ali Valiyev", "ali@mail.com", "ali123", datetime.now()),
#     ("Madina Karimova", "madina@gmail.com", "madina456", datetime.now()),
#     ("Bekzod Sodiqov", "bekzod@yahoo.com", "bekpass", datetime.now()),
#     ("Ozoda Alimova", "ozoda@mail.uz", "ozoda2025", datetime.now()),
#     ("Sardor Eshmatov", "sardor@inbox.uz", "sardor007", datetime.now())
# ]
#
# curr.executemany("INSERT INTO users (full_name, email, password, created_at) VALUES (%s, %s, %s, %s)", users_data)
# conn.commit()

# authors = [
#     ("Chingiz Aytmatov", "Qirg‘iziston"),
#     ("Abdulla Qodiriy", "O‘zbekiston"),
#     ("Jules Verne", "Fransiya"),
#     ("Mark Twain", "AQSh"),
#     ("Fyodor Dostoevskiy", "Rossiya")
# ]
# curr.executemany("INSERT INTO authors (full_name, country) VALUES (%s, %s)", authors)
# conn.commit()
# genres = [
#     ("Dasturlash",),
#     ("Ilmiy",),
#     ("Fantastika",),
#     ("Detektiv",),
#     ("Tarixiy",)
# ]
# curr.executemany("INSERT INTO genres (name) VALUES (%s)", genres)
# conn.commit()
# books = [
#     ("Yer", 16, "Tabiat va inson ruhiyati haqida roman", 1963, 6, 20250804),
#     ("Mehrobdan chayon", 17, "Tarixiy va fojiaviy sevgi romani", 1929, 7, 20250804),
#     ("20 ming mil suv ostida", 18, "Ilmiy-fantastik sarguzasht", 1870, 8, 20250804),
#     ("Tom Sawyer sarguzashtlari", 19, "Bolalar uchun sarguzasht roman", 1876, 9, 20250804),
#     ("Jinoyat va jazo", 20, "Psixologik va ijtimoiy roman", 1866, 10, 20250804)
# ]
#
# curr.executemany("""
#     INSERT INTO books (title, author_id, description, published_year, genre_id, created_at)
#     VALUES (%s, %s, %s, %s, %s, %s)
# """, books)
#
# conn.commit()

# comments = [
#     (1, 5, "Bu kitobni o‘qib hayratlandim!", datetime.now()),
#     (2, 6, "Sifatli asar, juda yoqdi", datetime.now()),
#     (3, 7, "Fan va hayolot uyg‘unligi ajoyib", datetime.now()),
#     (4, 8, "Bolalar uchun juda maroqli", datetime.now()),
#     (5, 9, "Og‘ir, ammo chuqur ma’noga ega", datetime.now())
# ]
# curr.executemany("""
#     INSERT INTO comments (user_id, book_id, content, reated_at)
#     VALUES (%s, %s, %s, %s)
# """, comments)
#
# conn.commit()

curr.execute("SELECT *FROM comments WHERE content IS NULL;")
a = curr.fetchall()
print(a)
