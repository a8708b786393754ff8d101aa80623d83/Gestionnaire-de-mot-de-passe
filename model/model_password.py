from .model_base import ModelMain

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
