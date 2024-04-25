from app_ import App


trigger = True
app = App(trigger=trigger)
app.load_data_json(path="data.json")

while trigger:
    app.Menu_show()
    input, valid = app.get_user_input()
    trigger = app.execute_option(user_input=input, valid=valid)