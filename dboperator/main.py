from db import db_connect
conn=db_connect()
cur=conn.cursor()
conn.autocommit=True

# cur.execute(
#     "CREATE DATABASE students"
# )
# print("Ma'lumotlar bazasi yaratildi")

# cur.execute(
#     """CREATE TABLE students(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     score INT
#     )"""
# )
# print("ok")

# cur.execute(
#     "INSERT INTO students(name,score)VALUES('Rayhona', 97),('Sevinchoy', 100), ('Dilnura',36)"
# )
# print("Ma'lumot qo'shildi")

cur.execute(
    "SELECT * FROM students WHERE name ILIKE 'R%'"
)
rows = cur.fetchall()
for row in rows:
    print(row)