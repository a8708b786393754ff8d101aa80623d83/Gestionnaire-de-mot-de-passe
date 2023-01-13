from .view_base import View


class ViewCredentials(View):
    def __init__(self):
        super().__init__()

    def insert(self):
        """Affiche que les données sont inserée """

        print('Les donnée sont insérer')

    def password_entry(self):
        """Request the password

        Returns:
            string: password entry 
        """

        self.password = input('Entrez le mot de passe maitre : ').strip()
        return self.password
