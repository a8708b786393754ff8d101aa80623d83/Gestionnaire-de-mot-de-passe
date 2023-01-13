from hashlib import sha512

from .controller_base import ControllerBase


class ControllerPassword(ControllerBase):
    def __init__(self, view, model_password):
        super().__init__(view)
        self.__models_secret = model_password('secret.db')
        self.__password_db = self.__models_secret.get_password()

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
