import psycopg2 as ps

con = ps.connect(
    user="root",
    password="example",
    host="db",
    port=5432
)