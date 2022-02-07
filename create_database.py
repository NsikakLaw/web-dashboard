import sqlite3
from sqlite3 import Error
from databaseconnections import create_db_connection


class Database:
    """ create a database connection to sqlite and
        run create and insert queries

    :param filename: database file name
    """

    def __init__(self, filename):
        self.filename = filename
        self.db_connection = create_db_connection(self.filename)

    def create_table(self, sql_create_table):
        """create sql table in the database
        :param sql_create_table: sql create table statement
        :return Successful or not
        """

        try:
            c = self.db_connection.cursor()
            c.execute(sql_create_table)
            return "Successful!"

        except Error as e:
            print(e)

    def insert_table(self, table_name, schema, values):

        """Create insert statement to the database
        :param table_name: table name
        :param schema: columns of the table table
        :param values: values to be inserted into the table
        :return success or error string
        """

        sql_query = '''INSERT INTO ''' + table_name + '''(%s''' % ', '.join(schema) \
                    + ''') VALUES (%s''' % ', '.join(['"' + str(e) + '"' for e in values]) + ''');'''

        try:
            c = self.db_connection.cursor()
            c.execute(sql_query)
            self.db_connection.commit()
            return "Success!"

        except Error as e:

            return "Error! could not insert into " + table_name
