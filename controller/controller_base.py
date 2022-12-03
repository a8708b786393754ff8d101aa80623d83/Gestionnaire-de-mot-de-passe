from hashlib import sha512

class ControllerBase:
    def __init__(self, view, model_credentials, model_password):
        self.view = view()
        self.__model_credentials = model_credentials('user.db')
        self.__models_secret = model_password('secret.db')
        self.__password_db = self.__models_secret.get_password()
        self.__loop_cmd = False
        self.credentials = {
            'service': None,
            'user': None,
            'password': None
        }

    def first_time(self):
        """Checks if the password has already been created 
            (if it is stored in the secret database)

        Returns:
            bool: True if it has just created succeed, if it has already been created
        """
        if self.__password_db == None and self.view.password != None:
            self.__password_db = self.encrypt_password(
                self.view.password)  # hash le mot de passe qui est entrez
            # ajoute le mot de passe qui est entrer
            self.__models_secret.set_password(self.__password_db)
            print('Mot de passe maitre creer')
            return True
        return False

    def encrypt_password(self, password: str):
        """Encrypt passord 

        Args:
            password (str): password entry  

        Returns:
            tuple: string which is hash
        """
        return sha512(bytes(password, 'utf-8')).hexdigest()

    def verif_password(self):
        """Check password hash is same as master password (store password is hash)

        Returns:
            bool: True if the entered password matches, false if it does not match
        """
        if self.view.password != None:
            if sha512(bytes(self.view.password, 'utf-8')).hexdigest() == self.__password_db[0]:
                return True
            return False

    def show(self):
        """Displays the element
        stored in the user table
        """
        data = self.__model_credentials.get_credentials()
        self.view.show_all_info(data)

    def set_command(self):
        """Interaction with user inputs
        """
        self.__loop_cmd = True
        while self.__loop_cmd:
            cmd = input('>> ').strip()

            if "set" in cmd:
                cmd = cmd.split(' ')
                if len(cmd) == 4:
                    self.credentials['service'] = cmd[1]
                    self.credentials['user'] = cmd[2]
                    self.credentials['password'] = cmd[3]

                    self.__model_credentials.set_credentials(self.credentials)
                    print("Les donnée sont inserer")

                else:
                    print(self.view.help)

            elif cmd == 'show':
                self.show()

            elif cmd in ['exit', 'q', 'quit']:
                self.__loop_cmd = False

            else:
                print(self.view.help)
