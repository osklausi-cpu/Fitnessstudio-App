# Aufgabe 16
# Du findest ein Dictionary mit 5 Studenten und deren Noten.

studenten = {
    "tim": 2,
    "tom": 1,
    "timi": 4,
    "tommy": 2,
    "timo": 5
}

# Aufgabe 16.1
# Erstelle eine Funktion, die einen neuen Studenten und seine Note nach der Eingabe eines Benutzers in dem Dictionary speichert, allerdings nur, wenn weniger als
# 5 Studenten in dem Dictionary gespeichert sind.

def newStudent():
    if len(studenten) < 5: #len ist im Grunde die Abkürzung von „length“, also „Länge“.
        name = input("Name des Studenten: ")
        note = input("note des Studenten: ")
        studenten[name] = note
        print(f"{name} mit Note {note} wurde hinzugefügt.")
    else:
        print("Es können keine weiteren Studenten hinzugefügt werden. Maximum erreicht")
    
newStudent()
print(studenten)


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