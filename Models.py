import sqlite3

class ModelMain:
    def __init__(self, database: str, table: str):
        self.conn = sqlite3.connect(database)
        self.curs = self.conn.cursor()
        self.table = table

    def init_db(self):
        """try to read the table concerned if there is an error it will create it
        """
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


class ModelCredentials(ModelMain):
    """child class which will concern the operations of the user table

    Args:
        ModelMain (_type_): parent class 
    """
    def __init__(self, database: str, table: str = 'credentials'):
        super().__init__(database=database, table=table)
        self.init_db()

    def get_credentials(self):
        self.curs.execute(
            f'SELECT service, name, passwd FROM {self.table}')
        return self.curs.fetchall()

    def get_password(self):
        self.curs.execute(f'SELECT passwd FROM {self.table}; ')
        return self.curs.fetchall()

    def set_credentials(self, data: dict):
        self.curs.execute(f""" INSERT INTO  {self.table}(service, name, passwd)
                                    VALUES("{data["service"]}" , "{data["user"]}" , "{data["password"]}") """)
        self.conn.commit()

    def create_database(self):
        self.curs.execute(f"""
                            CREATE TABLE {self.table}
                            
                            (
                            name VARCHAR(30) NOT NULL,
                            passwd INT NOT NULL,
                            service VARCHAR NOT NULL) 
                                """)
        self.conn.commit()


class ModelPassword(ModelMain):
    def __init__(self, database: str, table: str = 'passwd'):
        super().__init__(database, table)
        self.init_db()

    def get_password(self):
        return self.curs.execute(f'SELECT password FROM {self.table}').fetchone()

    def create_database(self):
        self.curs.execute(f""" 
                        CREATE TABLE {self.table}                            
                        (password text NOT NULL)
                        """)
        self.conn.commit()

    def set_password(self, password_entry: str):
        self.curs.execute(f"""INSERT INTO {self.table} 
                            VALUES("{password_entry}")
                            """)
        self.conn.commit()
