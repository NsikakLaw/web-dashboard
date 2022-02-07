from create_database import Database
import json
import pandas as pd

with open('schema.json', 'r') as f:
    schema_dict = json.load(f)


def convert_csv_to_df(filename):
    df = pd.read_csv(filename)

    return list(df.columns), df


def create_db_details():
    new_db = Database("test.db")

    for i in schema_dict:
        new_db.create_table(schema_dict[i])

    members_df = convert_csv_to_df("csv/members.csv")
    menu_df = convert_csv_to_df("csv/menu.csv")
    sales_df = convert_csv_to_df("csv/sales.csv")

    for i in members_df[1].values:
        new_db.insert_table('members', members_df[0], i)

    for i in menu_df[1].values:
        new_db.insert_table('menu', menu_df[0], i)

    for i in sales_df[1].values:
        new_db.insert_table('sales', sales_df[0], i)


