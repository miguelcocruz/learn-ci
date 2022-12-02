import psycopg2 as ps



def connect():
    user = "root"
    password = "example"
    host = "db"
    port = 5432

    con = ps.connect(f'postgresql://{user}:{password}@{host}:{port}/')
    return con