#!/usr/bin/python3
from controller.controller_base import ControllerBase

from model.model_password import ModelPassword
from model.model_credentials import ModelCredentials

from view import View

c = ControllerBase(View, ModelCredentials, ModelPassword)
c.view.password_entry()  # demande du mot de passe
first_time_connected = c.first_time()

if not first_time_connected: # regarde si c'est la premiere fois qu'il se connecte
    if c.verif_password():
        c.set_command()

    else:
        print('Veuillez verifier mot de passe maitre ')