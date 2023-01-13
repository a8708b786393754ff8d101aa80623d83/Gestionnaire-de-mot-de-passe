import sqlite3


class ModelMain:

    def __init__(self, database: str, table: str):
        """Constructive method, it creates a database in the data folder.

        Args:
            database (str): name of databases
            table (str): table name
        """

        self.conn = sqlite3.connect("data/"+database)
        self.curs = self.conn.cursor()
        self.table = table

    def init_db(self):
        """try to read the table concerned if there is an error it will create it."""

        try:
            self.read()
        except sqlite3.DatabaseError:
            self.create_database()

    def read(self):
        """Read the table concerning

        Returns:
            list: element store in table
        """

        self.curs.execute(f'SELECT * FROM {self.table}')
        return [element for element in self.curs.fetchall()]

    def create_database(self):
        """
            Query create database here
        """

    def __del__(self):
        self.conn.close()
