#!/usr/bin/python3
from controller.controller_base import ControllerBase
from controller.controller_password import ControllerPassword
from controller.controller_credentials import ControllerCredentials


from model.model_password import ModelPassword
from model.model_credentials import ModelCredentials

from view.view_base import View
from view.view_credentials import ViewCredentials


def command_prompt():
    """Interaction with user inputs"""

    while True:
        cmd = input('>> ')
        if 'set' in cmd:
            cmd_split = cmd.split(' ')
            if len(cmd_split) == 4:
                controller_credentials.credentials['service'] = cmd_split[1]
                controller_credentials.credentials['user'] = cmd_split[2]
                controller_credentials.credentials['password'] = cmd_split[3]

                controller_credentials.set_credentials()
                controller_credentials.view.insert()
                
            else:
                controller_base.view.help()
        elif cmd == 'show':
            controller_credentials.show()

        elif cmd in ['exit', 'q', 'quit']:
            break

        else:
            controller_base.view.help()


controller_base = ControllerBase(View)
controller_credentials = ControllerCredentials(ViewCredentials, ModelCredentials)
controller_password = ControllerPassword(ViewCredentials, ModelPassword)

controller_password.view.password_entry()  # demande du mot de passe
first_time_connected = controller_password.first_time()

if not first_time_connected:  # regarde si c'est la premiere fois qu'il se connecte
    if controller_password.verif_password():
        command_prompt()
    else:
        print('Veuillez verifier mot de passe maitre ')
