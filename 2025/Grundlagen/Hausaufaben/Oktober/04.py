# Aufgabe 1
# Erstelle eine Liste von Quadratzahlen der Zahlen von 1 bis 20

for quadratzahl in range (1,21):
    print(quadratzahl **2)
 
 
# Aufgabe 2
# Hier ist eine Liste von graden Zahlen. Verwende eine List Comprehension um nur die
# geraden Zahlen herauszufiltern
 
zahlen = [10, 15, 23, 42, 55, 68, 73, 80, 87, 93, 96, 99, 110, 111, 120]

gerade_zahlen = [zahl for zahl in zahlen if zahl % 2 == 0]

print(gerade_zahlen) 

# for zahl for in zahlen- geht jedes Element in der Liste durch
# [zahl...] - wäre hier eine variable 
#if zahl % 2 == 0 → filtert nur die Zahlen, die ohne Rest durch 2 teilbar sind


# Aufgabe 3
# Du findest eine Variable vom Datentyp String, Erstelle eine neue Liste die nur die Vokale a, e, i, o, u aus dem String enthält
 
satz = "Zehn zahme Ziegen zogen zehn Zentner Zucker zum Zoo"

neue1 = [li for li in satz if li.lower() in "aeiou"]

print(neue1)

# macht alle Großbuchstaben klein
 
# Aufgabe 4
# Erstelle eine Liste mit den Zahlen 1 bis 100, aber nimm nur die Zahlen auf, welche durch 5 oder 7 teilbar sind
zahlen = [x for x in range(1,101) if x % 5 ==0 or x % 7==0 ]
print(zahlen)

# Das ist die Grundstruktur einer List Comprehension. 
# for x in range(1, 101) → sagt: „Nimm nacheinander jede Zahl x von 1 bis 100.“
# x ganz vorne → sagt: „Füge genau diesen Wert x in die neue Liste ein.“


# Aufgabe 5
# Du findest eine Liste mit Wörtern. Erstelle eine neue Liste die nur Wörter enthält die länger als 4 Zeichen lang sind
 
woerterliste = ['Apfel', 'Ei', 'Banane', 'Traube', 'Ananas', 'Kiwi', 'Uwe', 'Rettungswagen', 'Schlafmütze']

neu =[wort for wort in woerterliste if len(wort) >=4]
print(neu)

# for wort in woerterliste   - geht jedes Wort in der Liste durch
# if len(wort) >=4           - überprüft, ob das Wort mindestens 4 Buschtaben hat
# wort for wort in ...if..   - erstellt die neue Liste nur mit den Wörtern, die die Bedingung erfüllen


# Aufgabe 6
# Du findest einen Satz. Erstelle eine Liste, die die Länge jedes Wortes in diesem Satz erhält
 
satz = "Ihr werdet besser und besser. Hört nicht auf zu lernen, ihr seid richtig gut <3"
 
 
# Aufgabe 7
# Erstelle eine Liste der Quadratzahlen von 1 bis 50, aber nur für ungrade Zahlen

neu = [zahl ** 2 for zahl in range(1, 51) if zahl % 2 == 1]
print(neu)
 
 
# Aufgabe 8
# Du findest eine Liste mit Wörtern. Erstelle eine Liste, in der jedes Wort in Großbuchstaben umgewandelt wird
 
wortliste = ["Das", "ist", "eine", "sehr", "einfache", "Übung", "um", "dir", "das", "Leben", "schwer", "zu", "machen"]

gross = [wort.upper() for wort in wortliste]
print(gross)
 
 
# Aufgabe 9
# Du findest 2 Listen. Erstelle eine neue Liste von Tupeln, die alle Kombinationen von Zahl und Buchstaben enthalten
 
zahlen = [1, 2, 3]
buchstaben = ['A', 'B', 'C']
 
 
# Aufgabe 10
# Du findest eine Liste mit 1000 Namen. Baue ein Programm, in dem ein Benutzer einen Namen eigeben muss. Benutze die List Comprehension dazu,
# die Namensliste nach dem Namen zu durchsuchen unabhängig davon, ob der Benutzer den Namen groß oder klein schreibt.
# Messe die Zeit wie lange deine List Comprehension dafür benötigt hat.
# Gib auch an wie oft der Name in der Liste vorhanden ist.