from create_details import create_db_details


def test_create_db_details():

    assert str(type(create_db_details())) == "<class 'create_database.Database'>"
