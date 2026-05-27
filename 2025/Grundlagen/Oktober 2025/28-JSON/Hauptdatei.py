from get_all_users import alleMitarbeiter    #von aufgabe 3 
liste = alleMitarbeiter()  # funktion braucht immer eine Variable, damit man die auch z.B. in der For Schleife benutzen kann
from save_user import saveUser 

#Aufgabe 1
print("""===== Hauptmenü =====
1: Mitglieder Liste lesen
2: Mitglied hinzufügen
3: Mitglied bearbeiten
4: Mitglied entfernen""")


#Aufgabe 4
auswahl = int(input("Bitte wähle einen Zahl aus: "))

if auswahl == 1:
    for mitglied in liste:
        print(f"Name: {mitglied['name']}, Alter: {mitglied['alter']}, Email: {mitglied['email']}")

elif auswahl == 2:
    saveUser()#---> funktion ausführen
else:
    print("ungültige eingabe")
    


