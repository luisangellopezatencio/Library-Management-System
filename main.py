from app_ import App
from colorama import Fore


trigger = True
app = App(trigger=trigger)
app.load_data_json(path="data.json")
print(Fore.MAGENTA + "Welcome to Library Management System")

while trigger:
    app.Menu_show()
    input, valid = app.get_user_input()
    trigger = app.execute_option(user_input=input, valid=valid)