# '''''''''''''# Aufgabe 1
# # Erstelle ein Dictionary, das die Noten eines Schülers in verschiedenen Fächern speichert.
# # Schreibe ein Programm, das die Note für ein Fach abfragt und ausgibt. Verwende get() und
# # fange mit if und else einen Fehler ab, falls das Fach nicht existiert.

noten = {               
     "mathe": 1,      # Schlüssel: "mathe"  Wert: 1
     "englisch": 2,
     "biologie": 3
 }

fach = input("Für welches Fach möchtest du die note wissen? ")
note = noten.get(fach) # .get() gibt None zurück, wenn das Fach nicht existiert

if note is None:
    print("Fehler: Fach nicht gefunden")
else:
    print(f"Die Note in {fach} ist: {note}")

# # AUfgabe 2
# # Erstelle ein Dictionary mit den Namen von 5 Mitarbeitern und ihren Positionen in einem Betrieb.
# # Schreibe ein Programm, das einen Benutzer nach dem Namen fragt und entweder die Position des
# # Mitarbeiters ausgibt oder "Mitarbeiter konnte nicht gefunden werden" anzeigt, wenn der Name
# # nicht im Dicitonary vorhanden ist (benutze get() )

mitarbeiter={
    "anna": "chefin",
    "ben": "manager",
    "tom": "verwalter",
    "tim": "sekretärin",
    "orkan": "techniker"

}

name= input("Bitte geben sie einen namen ein: ")      # ➡️Das Programm fragt den Benutzer nach einem Namen.
position= mitarbeiter.get(name)

if position is None:
    print("Mitarbeiter konnte nicht gefunden werden")
else:
    print(f"Die position von {name} ist {position}")
 
 
# # Aufgabe 3
# # Erstelle ein Dictionary, das 5 Lebensmittel und ihre Preise enthält. Baue eine Funktion, die neue Produkte und
# # deren Preise speichert. Erweitere deine Funktion, indem du nach einem
# # Artikel suchst und gib ihn mit seinem Preis aus. Wenn der Artikel nicht gefunden wurde, soll der Artikel gespeichert werden und einen
# # Standardpreis von 0 zurückgegeben
 
lebensmittel = {
    "bananen": "1 euro",
    "kiwis": "2 euro",
    "äpfel": "3 euro",
    "gurken": "4 euro",
    "orangen": "5 euro"
}

def funktion(lebensmittel):
    # Nutzer gibt einen Artikel ein
    artikel = input("Welchen Artikel möchtest du sehen? ").lower()

    if artikel in lebensmittel:
        print(f"{artikel.capitalize()} kostet {lebensmittel[artikel]}.")
    else:
        lebensmittel[artikel] = "0 euro"
    print(f"{artikel.capitalize()} war nicht vorhanden. Es wurde mit Preis 0 euro hinzugefügt.")

# Funktion aufrufen
funktion(lebensmittel)


# # Aufgabe 4
# # Erstelle ein Dicitonary mit dem Namen und dem Alter von 3 Personen. Schreibe ein Programm, das durch die Schlüssel des
# # Dictionaries iteriert und nur die Namen der Personen ausgibt

personen = {
    "abdi" : 1,
    "sevret": 2,
    "mahmud": 3
}

for schlüssel in personen:
    print(schlüssel)

 
# Aufgabe 5
# Gegeben ist ein Dictionary, das die Lagerbestände eines Geschäfts speichert.
# Schreibe ein Programm, das alle Artilkel ausgibt, die aktuell im Lager sind
# (Tipp: Schlüssel mit Wert > 0)
 
 
articles = {
    "Screws": 10000,
    "Wood": 0,
    "Nails": 100,
    "toolkit": 10,
    "scanner": 2,
    "paper": 0,
}

for artikel,anzahl in articles.items():
    if anzahl > 0:               #: dann
        print(f"Wir haben {artikel} so oft auf Lager {anzahl} ")
    else:
        print(f"Wir haben diesen {artikel} 0 mal")
 
 
# Aufgabe 6
# Du findest ein Dictionary mit Ländern als Schlüssel und deren Bevölkerungszahlen als Wert.
# Schreibe ein Programm, das die Länder nach Namen sortiert und in alphabetischer Reihenfolge
# die Namen ausgibt
 
countries = {
    "Deutschland": 85000000,
    "Frankreich": 68000000,
    "Spanien": 47000000,
    "Polen": 36000000,
    "Albanien": 3000000
}
 
for land in sorted(countries):
    print(land)

 
# Aufgabe 7
# Erstelle ein Dictionary mit fünf Tieren und deren Anzahl im Lager aus einem Tierhandel. Schreibe ein
# Programm, das die Summe aller Werte im Dicitonary berechnet und ausgibt.

lager = {
    "katze": 1,
    "hund":2,
    "Pferd": 3,
    "Kuh": 4,
    "maus": 5
}
summe=0
for tier in lager:                        #➡️ tier ist der Schlüssel
    summe = summe + lager[tier]           #➡️ addiere den Wert
print(summe)

# Aufgabe 8
# Du findest ein Dictionary mit den Namen von Schülern als Schlüssel und deren Noten als Werte.
# Schreibe ein Programm, das den Notendurchschnitt aller Noten berechnet (benutze values() und keys())
 
students = {
    "Alan": 1,
    "Jacques": 6,
    "Gerhard": 1,
    "Willi": 4,
    "Susanne":2
}
mittelwert = sum
 
# Aufgabe 9
# Erstelle ein Dictionary, das den Umsatz verschiedener Filialen eines Unternehmens speichert.
# Nutze den Filialnamen als Schlüssel und den Umsatz als Wert.
# Schreibe ein Programm, das die Filiale mit dem höchsten Umsatz identifiziert und den Namen
# der Filiale sowie den Umsatz ausgibt
 
umsatz={
    "Bershka": 100000,
    "Zara": 199999,
    "primark": 230000
}
# finde den Schlüssel (Filiale) mit dem größten Wert (Umsatz)
beste_filiale=  max(umsatz, key=umsatz.get)

# Aufgabe 10
# Erstelle ein Dictionary, welches die Preise von 5 Artikeln speichert. Verwende items() um durch die Schlüssel Wert Paare zu iterieren
# und alle Artikel, deren Preis über 10 € liegt, auszugeben

preise = {
    "fanta": 3,
    "brot": 11,
    "käse": 4,
    "wurst": 1,
    "apfel": 2
}

for schlüssel, preis in preise.items():
    if preis > 10:
        print(schlüssel, preis, "€")


#➡️ preise.items() gibt Paare wie ("fanta", 3) zurück.
#➡️ artikel bekommt den Namen, preis den Wert.
#➡️ keys() → nur die Schlüssel
#➡️ values() → nur die Werte
#➡️ items() → beides zusammen (Schlüssel und Wert)
 


# Aufgabe 11
# Erstelle ein Dictionary, das die Punktzahl von Spielern in einem Videospiel speichert.
# Der Spielername ist der Schlüssel und die Punktzahl der Wert. Schreibe ein Programmm, welches den Spieler ausgibt,
# der die höchste Punktzahl hat. (Benutze items())

spieler={
    "anton": 32,
    "ben": 23,
    "tim": 21
}

meiste_punkte =  max(spieler, key=spieler.get)
print(meiste_punkte)

# ➡️ max() sucht den größten Wert.
# ➡️ Mit key=spieler.get sagst du Python: „Benutze die Punktzahl jedes Spielers, um zu vergleichen.“
# ➡️ So bekommst du den Namen des Spielers mit der höchsten Punktzahl.


# AUfgabe 12
# Erstelle ein Dictionary mit Informationen über einen Film (z.B.: Titel, Jahr, Genre). Schreibe ein Programm dass das Dictionary
# mithilfe von update um die Bewertung des Films erweitert.

film = {
    "titel": "avatar",
    "jahr": 2003,
    "genre": "fantasy"
}

film.update({"bewertung": "gut"}) # Mit der Methode .update() fügst du ein neues Schlüssel-Wert-Paar hinzu:
                                  # "bewertung": "gut"
print(film)
 
 
# Aufgabe 13
# Erstelle 2 Dictionaries die jeweils den Lagerbestand in zwei verschiedenen Filialen eines Geschäfts darstellen.
# Schreibe ein Programm das den Lagerbestand der beiden Filialen zusammenführt (benutze Update) und gib das
# kombinierte Dicitonary aus
 
filiale1= { "Jeans": 200,
            "t-shirt": 300,
            "jacken": 211

}
filiale2={
    "pullover": 23,
    "socken": 33
}

filiale1.update(filiale2)
print(filiale1)

# Erklärung:
# ➡️ Du hast zwei Dictionaries (filiale1, filiale2) mit Artikeln und Beständen.
# ➡️ Mit filiale1.update(filiale2) werden alle Schlüssel–Wert-Paare aus filiale2 zu filiale1 hinzugefügt.



# Aufgabe 14
# Du findest ein Dictionary mit Produkten und ihren Preisen Schreibe ein Programm, das den Benutzer auffordert, den Preis eines Produkts zu
# aktualisieren. Verwende update() um das Produkt mit dem neuen Preis im Dicitonary zu aktualisieren.
# Benutzer auffordern, Produkt und neuen Preis einzugeben

# Beispiel-Dictionary
produkte = {
 #Schlüssel  #Wert 
    "Apfel": 1.2,
    "Banane": 0.8,
    "Milch": 2.5,
    "Brot": 1.8
}

# Benutzer auffordern, Produkt und neuen Preis einzugeben
produkt = input("Welches Produkt möchtest du aktualisieren? ")
neuer_preis = float(input("Neuer Preis: "))

# Preis mit update() ändern
produkte.update({produkt: neuer_preis})

print("Aktualisiertes Dictionary:", produkte)
 
# Aufgabe 15
# Erstelle ein Dictionary mit dem Namen von drei Klassenkameraden und deren Handynummern. Schreibe ein Programm,
# dass das Dicitonary mit clear() leert und überprüft, ob es nun leer ist.
 
klassenkameraden = {
    "ben": "0157 44785964",
    "anna": "0157 44875685",
    "tim": "0157 48447856"

}

klassenkameraden.clear() # dictionary leeren

#überprüfen ob leer ist
if not klassenkameraden:     # ➡️„Wenn klassenkameraden nicht voll ist, dann …“
    print("Das Dictionary ist jetzt leer:", klassenkameraden)
else:
    print("Das Dictionary ist noch nicht leer:", klassenkameraden) #➡️Das Komma in print() trennt verschiedene Dinge, die man ausgeben will.

# ➡️Ein Dictionary ist False, wenn es leer ist, und True, wenn es Einträge hat. Deshalb benutzt man not:



# Aufgabe 16
# Du findest ein Dictionary mit 5 Studenten und deren Noten.

studenten = {
    "tim"= 2,
    "tom"= 1,
    "timi"= 4,
    "tommy"= 2,
    "timo"=
}
# Aufgabe 16.1
# Erstelle eine Funktion, die einen neuen Studenten und seine Note nach der Eingabe eines Benutzers in dem Dictionary speichert, allerdings nur, wenn weniger als
# 5 Studenten in dem Dictionary gespeichert sind.


# Aufgabe 16.2
# Falls schon 5 Studenten in dem Dicitonary gespeichert sind, weise darauf hin, dass schon 5 Studenten gespeichert sind und
# stelle den Benutzer vor eine Wahl, ob er das aktuelle Dictionary löschen möchte um den neuen Studenten dort abspeichern zu können, gib währenddessen den
# Notendurchschnitt aller Studenten aus.
# Aufgabe 16.3
# Wenn der Benutzer sich gegen das Löschen der Daten entscheidet, beende das Programm.
# Aufgabe 16.4
# Wenn der Benutzer die Daten löschen will, rufe eine neue Funktion die du jetzt neu bauen wirst auf,
# welche als Parameter die Daten des neuen Studenten als Dictionary empfängt,
# Aufgabe 16.5
# lösche in deiner neuen Funktion, die du sinnvoll benannt hast alle Daten in dem Dicitonary student_graduations
# Aufgabe 16.6
# Stelle den Benutzer noch einmal in deiner neuen Funktion vor eine Auswahl, ob er die Daten die du Übergeben hast, in dem Dictionary student_graduations speichern will.
# Entscheidet sich der Benutzer die Daten zu speichern, speichere die neuen Daten in dem Dicitonary und gib dein Dictionary aus.
# Entscheidet sich der Nutzer gegen das speichern, sollte ein leeres Objekt angezeigt werden