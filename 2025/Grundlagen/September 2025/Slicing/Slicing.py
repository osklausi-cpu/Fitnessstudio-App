"""est_liste = [1,2,3,4,5,6,7,8,9,10]

teilbereich = test_liste[1:4] # [StartIndex:EndIndex]
teilbereich_rueckwaerts = test_liste[-5:-1] # Bildet einen Teilbereich aus einem hinteren Teil der Liste
teilbereich_rueckwaerts2 = test_liste[-1:-5:-1] # Bildet einen Teilbereich aus einem hinteren Teil der Liste aber Rückwärts durch die Schrittweite
teilbereich_2er_schritte = test_liste[::2] # Listenteilbereich in 2er Schritten
teilbereich_4er_schritte = test_liste[::4] #Teilbereich Anfang der Liste bis Ende in 4er Schritten

print(teilbereich)
print(teilbereich_rueckwaerts)
print(teilbereich_rueckwaerts2)
print(teilbereich_2er_schritte)
print(teilbereich_4er_schritte)"""

strings = [
    "Hund",
    "Katze",
    "Maus",
    "Vogel",
    "Schlange",
    "Elefant",
    "Giraffe",
    "Löwe",
    "Tiger",
    "Bär",
]

# Was sind die Ausgaben?:
# Aufgabe 1     strings[0:3]
# Aufgabe 2     strings[3:7]
# Aufgabe 3     strings[5:]
# Aufgabe 4     strings[2:-1]
# Aufgabe 5     strings[:4]
# Aufgabe 6     strings[-5:]
# Aufgabe 7     strings[1:8:2]
# Aufgabe 8     strings[::4]
# Aufgabe 9     strings[-4:-1]
# Aufgabe 10    strings[-3:]
# Aufgabe 11    strings[2:-2:3]
# Aufgabe 12    strings[1::2]
# Aufgabe 13    strings[:5:2]
# Aufgabe 14    strings[-6:-2:2]
# Aufgabe 15    strings[::5]
# Aufgabe 16    strings[3:-3]
# Aufgabe 17    strings[4:9:3]
# Aufgabe 18    strings[-8:-2:3]

print(strings[0:3])
print(strings[3:7])
print(strings[5:])
print(strings[2:-1])
print(strings[:4])
print(strings[-5:])
print(strings[1:8:2])
print(strings[::4])
print(strings[-4:-1])
print(strings[-8:-2:3])
