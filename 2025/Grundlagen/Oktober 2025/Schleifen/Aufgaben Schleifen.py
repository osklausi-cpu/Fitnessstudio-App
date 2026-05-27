# Aufgabe 1
# Schreibe eine for Schleife, die die Summe aller Zahlen von 1 bis 100 berechnet und das Ergebnis ausgibt

summe = 0

for zahl in range(1, 101):
    summe +=zahl  #summe += zahl
print("Die Summe von 1 bis 100 ist:", summe)

#Wenn du summe += i in einer Schleife benutzt, passiert Folgendes automatisch bei jedem Durchlauf der Schleife:
#Python nimmt den aktuellen Wert von summe.
#Addiert den aktuellen Wert von i dazu.
#Speichert das Ergebnis wieder in summe.
#Geht zur nächsten Zahl (i wird automatisch von der for-Schleife erhöht).
#Du musst nicht selbst jede Zahl addieren – die Schleife macht das automatisch Schritt für Schritt.

 
#Aufgabe 2
# Schreibe ein Programm, das eine Liste von Benutzernamen durchläuft und überprüft ob sie gültig sind
# Ein Benutzername ist nur gültig, wenn er länger als 3 Zeichen ist und keine Leerzeichen enthält

liste = ["Bob", "Tim", "Denis"]

for name in liste:
    if  len(liste) <=3:
        print(f"{name} ist gültig")



# Liste von Benutzernamen
benutzernamen = ["Max", "Anna123", "Jo", "Peter Pan", "Lena"]
# Schleife durch die Liste
for name in benutzernamen:
    # Überprüfen, ob der Name länger als 3 Zeichen ist und keine Leerzeichen enthält
    if len(name) > 3 and " " not in name:
        print(f"'{name}' ist gültig.")
    else:
        print(f"'{name}' ist ungültig.")
 
# Aufgabe 3
# Erstelle ein Programm, das eine Einkaufsliste verwaltet. Es sollte Artikel von einer Liste entfernen,
# wenn sie bereits gekauft wurden. Verwende dazu eine Schleife, um den Benutzer zu fragen,
# welchen Artikel er gekauft hat, und entferne diesen dann aus der Liste.
 
einkaufliste = ["Milch", "Brot", "Eier", "Äpfel", "Käse"]

while len(einkaufliste) > 0:                             
    print("\nEinkaufliste:", einkaufliste)
    gekauft = input("Welchen Artikel hast du gekauft? ")


#len(einkaufsliste) gibt dir die Anzahl der Artikel in der Liste.
#Solange diese Anzahl größer als 0 ist (> 0), heißt das: „Es gibt noch Artikel → Schleife läuft weiter“.
#Sobald len(einkaufsliste) == 0 (also keine Artikel mehr drin), wird die Bedingung falsch → die Schleife hört auf.

 
# Aufgabe 4
# Schreibe ein Programm, das so lange Noten (Zahlen zwischen 1 und 6) vom Benutzer entgegennimmt, bis der Benutzer "0" eingibt.
# Anschließend soll das Programm die Durchschnittsnote berechnen und ausgeben.
 
 
# Aufgabe 5
# Schreibe ein Programm, das eine zufällige Zahl zwischen 1 und 20 generiert.
# Der Benutzer soll die Zahl erraten. Wenn der Benutzer richtig rät, beende die Schleife.
# Ansonsten gib Hinweise aus, ob die Zahl zu hoch oder zu niedrig ist.
 
 
# Aufgabe 6
# Schreibe ein Programm, das vom Benutzer eine Reihe von Zahlen entgegennimmt.
# Verwende eine Schleife, um diese Eingaben zu verarbeiten und negative Zahlen herauszufiltern.
# Gib nur die positiven Zahlen in einer Liste aus.
 
 
# Aufgabe 7
# Baue eine Liste mit 8 Namen
# Schreibe ein Programm mit einer Funktion, welche einen Namen in einer Namensliste scuht, benutze hierfür eine Schleife die durch die Liste iteriert.
# Der Benutzer soll einen Namen in einem Input angeben können.
# Wenn du den Namen gefunden hast, füge dem Namen den Satz : " ist 25 Jahre alt" durch einen weiteren Input hinzu und speichere den Namen mit dem Alter in der Liste
# verwende die time.sleep() Methode um eine Bearbeitungszeit zu simulieren
# nach der simulation der Bearbeitungszeit, gib deine aktualisierung aus.
# Wenn der Name nicht in der Liste ist, gib aus, das der Name in er Liste nicht vorhanden ist