# AB Password Manager
Password manager, passwords are hashed before being stored.
No dependencies are needed for this tool.
## Use
You just need to run the main.py file.
```sh
python3 main.py
```
Once the script is executed, it asks for a master password, this password will be asked for each execution of the script.
## The commande
Once you have mastered the password, you will have a command prompt, you can type the command help to see all the commands available.
- help: list of commande
- show: display the content of the database give
- set: add a service, username/email and password

The syntax of the set command:
```sh
set  <service> <username/email> <password>
```

### Disclaimer
The project is under development but remains functional