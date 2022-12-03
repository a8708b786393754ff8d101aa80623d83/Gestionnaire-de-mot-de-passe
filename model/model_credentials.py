from .model_base import ModelMain

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
