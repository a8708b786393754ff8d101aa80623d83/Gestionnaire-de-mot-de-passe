import Controller

c = Controller.ControllerBase()
c.view.password_entry()  # demande du mot de passe
first_time_connected = c.first_time()

if not first_time_connected: # regarde si c'est la premiere fois qu'il se connecte
    if c.verif_password():
        c.set_command()

    else:
        print('Veuillez verifier mot de passe maitre ')