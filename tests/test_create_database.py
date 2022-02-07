from create_database import Database
import pytest
import json

with open('schema.json', 'r') as f:
    schema_dict = json.load(f)


@pytest.mark.parametrize(
    "table_name,output",
    [
        ("members", 'Successful!'),
        ("sales", 'Successful!')
    ]
)
def test_create_table(table_name, output):
    db = Database("test.db")

    assert db.create_table(schema_dict[table_name]) == output


def test_insert_table():

    db = Database("test.db")

    assert db.insert_table('members', ['customer_id', 'customer_name', 'join_date'],
                           ['A', 'Anna', '2021-11-15']) == "Error! could not insert into members"
