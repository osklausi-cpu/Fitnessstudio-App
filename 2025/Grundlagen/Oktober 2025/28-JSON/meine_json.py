import json
 
 
def open_json():
    with open("./test.json", "r", encoding="utf-8") as user: # open öffnet die Datei als Objekt
        user_list = json.load(user) # json.load() holt sich die JSON Daten aus dem Objekt
       
        for user in user_list: # Zugriff auf die umgewandelten Daten
            print(user["name"])
 
 
""" open_json() """
 
 
def save_user():
    new_user = {
        "name": "Dilek",
        "alter": 25
    }
    new_user_list = [] # Liste mit Daten (Daten normalerweise aus bestehendem JSON)
    new_user_list.append(new_user) # Anhand des neuen Datensatzes an die bestehenden Daten
    with open("./test.json", "w", encoding="utf-8") as data: # Modus "w" überschreibt die Daten aus dem JSON (In dem Fall alte plus neue Daten)
        user_list = json.dump(new_user_list, data)  #json.dump speichert die Daten in dem JSON
        print(user_list)
 
save_user()