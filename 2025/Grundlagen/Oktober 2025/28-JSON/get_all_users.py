import json
import os

# Pfad zur users.json relativ zu dieser Datei
pfad = os.path.join(os.path.dirname(__file__), "users.json")

def alleMitarbeiter():
    with open(pfad, "r", encoding="utf-8") as paket:
        mitarbeiter = json.load(paket) #unbedingt json importieren sonts klappt nicht
        return mitarbeiter
alleMitarbeiter()



#json.load werte lesen aus der json datei.

# pfad = os.path.join(os.path.dirname(__file__), "users.json")
# __file__ → sagt Python: „Hier bin ich, das ist die aktuelle Datei (get_all_users.py)“
# os.path.dirname(__file__) → fragt: „In welchem Ordner liegt diese Datei?“
# os.path.join(..., "users.json") → sagt: „Nimm diesen Ordner und füge users.json daran an“
# ✅ Ergebnis: Python weiß genau, wo die users.json ist, auch wenn du das Skript von einem anderen Ordner startest.
# Kurz gesagt:
# „Finde die users.json im gleichen Ordner wie meine Python-Datei.“

