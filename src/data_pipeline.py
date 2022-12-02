import psycopg2 as ps



def connect():
    con = ps.connect(
        user="root",
        password="example",
        host="db",
        port=5432
    )
    return con