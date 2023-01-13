from .controller_base import ControllerBase


class ControllerCredentials(ControllerBase):
    def __init__(self, view, model_credentials):
        super().__init__(view)
        self.__model_credentials = model_credentials('user.db')
        self.credentials = {
            'service': None,
            'user': None,
            'password': None
        }

    def set_credentials(self):
        """Set credentials with a model """

        self.__model_credentials.set_credentials(self.credentials)

    def show(self):
        """Displays the element
        stored in the user table
        """

        data = self.__model_credentials.get_credentials()
        self.view.show_all_info(data)
