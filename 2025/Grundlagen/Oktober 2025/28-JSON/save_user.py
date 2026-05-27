# Aufgabe 5
import json
import os
pfad = os.path.join(os.path.dirname(__file__), "users.json")
def saveUser():

    # users.json einlesen
    with open(pfad, "r") as file:
        userliste = json.load(file)

    # Eingaben abfragen
    name  = input("Name: ")
    alter = int(input("Alter: "))
    email = input("E-Mail: ")
    hobby = input("Hobby: ")

    # Neues Mitglied als Dictionary erstellen
    neues_mitglied = {
        "name": name,
        "alter": alter,
        "email": email,
        "hobby": hobby
    }

    # Neues Mitglied zur Liste hinzufügen
    userliste.append(neues_mitglied)

    # Aktualisierte Liste wieder speichern
    with open(pfad, "w") as file:
        json.dump(userliste, file, indent=4)

    print("Mitglied erfolgreich gespeichert!")
