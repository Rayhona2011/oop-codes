# from db import db_connect
# conn = db_connect()
# cur=conn.cursor()
# conn.autocommit=True

# cur.execute(
#     "CREATE DATABASE mahsulotlar"
# )
# print("ok")

# cur.execute(
#     """CREATE TABLE mahsulotlar(
#     id SERIAL PRIMARY KEY,
#     brand VARCHAR(100),
#     madel VARCHAR(100),
#     price NUMERIC(10,2)
#     )"""
# )
#  print("ok")

# cur.execute(
#     "INSERT INTO mahsulotlar(brand, madel , price)VALUES('Samsung','TV 90',1000000),('Artel','Muzlatgich', 10000000),('Samsung','Galaxy S26',16000000),('Apple','iPhone 15',20000000)"
# )
# print("ok")

# cur.execute(
    # "SELECT AVG(price) FROM mahsulotlar"
    # "SELECT MAX(price) FROM mahsulotlar"
    # "SELECT MIN(price) FROM mahsulotlar"
    # "SELECT COUNT(id) FROM mahsulotlar"
    # "SELECT SUM(price) FROM mahsulotlar"
    # "SELECT * FROM mahsulotlar WHERE brand  NOT IN ('Artel')"
    # "SELECT * FROM mahsulotlar WHERE brand  IN ('Artel')"

    # "SELECT * FROM mahsulotlar ORDER BY price DESC"
    # "SELECT *FROM mahsulotlar LIMIT 2"
    # "SELECT * FROM mahsulotlar WHERE price <> 1000000"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)


from db import db_connect
conn= db_connect()
cur = conn.cursor()
conn.autocommit = True

# cur.execute(
#     "CREATE DATABASE restaran"
# )
# print("ok")

# cur.execute(
#     """CREATE TABLE orders(
#     id SERIAL PRIMARY KEY,
#     products VARCHAR(100)
#     )"""
# )
# print("Jadval yaratildi")

# cur.execute(
#     "INSERT INTO orders(products)VALUES('Shourma')"
# )
# print("ok")

cur.execute(
    "SELECT COUNT(id), products FROM orders GROUP BY products"
)
rows = cur.fetchall()
for row in rows:
    print(row)