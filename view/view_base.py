class View:
    def __init__(self):
        self.password = None
        self.help = """ Commande introuvable  
                show: affiche ce que vous avez stocker
                set <service> <nom utilisateur/email> <mot de passe>: insert les donner """

    def password_entry(self):
        """Request the password

        Returns:
            string: password entry 
        """
        self.password = input('Entrez le mot de passe maitre : ').strip()
        return self.password

    def show_all_info(self, data: list):
        """show the element

        Args:
            data (list): list of warning elements of the database
        """
        for element in data:
            print('--------------')
            print(f'Service: {element[0]}')
            print(f"Email/nom d'utilisateur: {element[1]}")
            print(f'Mot de passe: {element[2]}')
        print('--------------')
        