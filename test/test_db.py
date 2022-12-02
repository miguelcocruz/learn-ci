import pytest

from src import data_pipeline

def test_insert():

    con = data_pipeline.connect()
    cursor = con.cursor()
    cursor.execute("""
        INSERT INTO users (id, name)
        VALUES (2, 'mc')
    """)

    cursor.close()
    con.commit()

    cursor2 = con.cursor()
    cursor2.execute("SELECT * FROM users")

    response = cursor2.fetchall()

    print (response)

    assert len(response) == 0