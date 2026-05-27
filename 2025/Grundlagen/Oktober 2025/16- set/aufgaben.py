
# Aufgabe 1
# Füge mit der `add()` Methode ein weiteres Tier, z.B. "Elefant", hinzu
tiere = {"Hund", "Katze", "Vogel"}

tiere.add()={"Elefant"}
print(tiere) 


# Aufgabe 2
# Entferne die Zahl 3 mit der `remove()` Methode
zahlen = {1, 2, 3, 4, 5}

zahlen.remove(3)
print(zahlen)
 

# Aufgabe 3
# Verwende `discard()` für die Farbe "blau" und gib dein set aus
farben = {"rot", "gelb", "grün", "schwarz", "weiß"}

farben.discard("blau")
print(farben)

# ✅ "blau" war gar nicht im Set → nichts wurde entfernt.
# ✅ discard() ist sicherer als remove(), weil es keinen Fehler auslöst, wenn das Element fehlt.

 
# Aufgabe 4
# Verwende `union()`, um ein Set mit allen Früchten und Gemüsen zu erstellen und gib es aus
obst = {"Apfel", "Banane", "Kirsche", "Pflaume", "Mango"}
gemüse = {"Karotte", "Tomate", "Salat", "Brokkoli", "Kartoffel"}

zusammen = obst.union(gemüse)
print(zusammen)

# ➡️union() erstellt ein neues Set, das alle Elemente aus beiden Sets (obst und gemüse) enthält.
# ➡️Doppelte Einträge werden automatisch entfernt (typisches Verhalten von Sets).
# ➡️Das Original-Set obst und gemüse bleiben unverändert.

 
# Aufgabe 5
# Verwende `intersection()` für die gemeinsamen Städte heruaszufiltern und gib sie aus
staedte = {"Berlin", "Hamburg", "München", "Köln", "Stuttgart"}
staedte2 = {"München", "Düsseldorf", "Berlin", "Leipzig"}

gemeinsam = staedte.intersection(staedte2)
print(gemeinsam)
 
 
# Aufgabe 6
# Verwende `difference()`, um die Sportarten zu finden, die nur in deinem Lieblings-Set sind
sportarten_studio1 = {"Fußball", "Basketball", "Tennis"}
sportarten_studio2 = {"Tennis", "Golf", "Schwimmen"}


sportarten = sportarten_studio1.difference(sportarten_studio2)
print(sportarten)


# Aufgabe 7
# Finde die Tiere, die nur in einem der beiden Gehege vorkommen (nicht in beiden).
 
gehege_1 = {"Löwe", "Tiger", "Elefant", "Zebra"}
gehege_2 = {"Tiger", "Elefant", "Giraffe", "Nashorn"}

tiere = gehege_1.symmetric_difference(gehege_2)
print(tiere)

# ➡️Erklärung:
#  symmetric_difference() gibt ein neues Set mit allen Elementen zurück, die nur in einem der Sets vorkommen, also nicht in beiden.



