from databaseconnections import *


def test_create_db_connection():

    assert str(type(create_db_connection("test.db"))) == "<class 'sqlite3.Connection'>"
