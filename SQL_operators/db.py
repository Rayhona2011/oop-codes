# import psycopg2
# def db_connect():
#     conn = psycopg2.connect(
#     host="localhost",
#     database="mahsulotlar",
#     user = "postgres",
#     password = "vorislar2026"
#     )
#     return conn


import psycopg2
def db_connect():
    conn = psycopg2.connect(
    host="localhost",
    database="restaran",
    user = "postgres",
    password = "vorislar2026"
    )
    return conn