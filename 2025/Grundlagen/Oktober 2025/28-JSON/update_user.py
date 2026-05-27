    # {
    #     "name": "Burak",
    #     "alter": 25,
    #     "email": "burak@outlook.de",
    #     "hobby": "Hobby Horsing"
    # },


import json
import os

pfad = os.path.join(os.path.dirname(__file__), "users.json")

def user_update():
    # 1. JSON lesen
    with open(pfad, "r") as file:
       userliste = json.load(file)

name = input("Name des Miglieds, das bearbeitet werden soll: ")


for mitglied in userliste:
    if name["name"].lower() == name.lower():
        print("Drücke ENTER, um den alten Wert zu behalten.\n")

        


 


# json.load() wird verwendet, um Daten aus einer JSON-Datei in Python einzulesen.'