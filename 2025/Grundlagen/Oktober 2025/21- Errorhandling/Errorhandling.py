def fehler_hinweis():
    print("Hier ist ein Fehler unterlaufen, bitte prüfe deine Eingabe nochmal")
    eingabe = input("Willst du das Programm neu starten?")
    if eingabe == "ja":
        test_function()
    else:
        print("Das Programm wurde beendet")
 
 
def fehler_hinweis_zerodivision():
    print("Das teilen durch 0 ist nicht möglich")
 
 
def test_function():
    try:
        zahl1 = int(input("Bitte eine Zahl eingeben: "))
        zahl2 = int(input("Bitte zweite Zahl eingeben: "))
        ergebnis = zahl1 / zahl2
        print(ergebnis)
    except (ValueError, ZeroDivisionError): # Auflisten mehrerer Exceptions als Tupel zusammengefasst für die Ausführung der gleichen Funktion
        fehler_hinweis()
   
       
 
 
 
test_function()

def fehler_hinweis():
    print("Hier ist ein Fehler unterlaufen, bitte prüfe deine Eingabe nochmal")
    eingabe = input("Willst du das Programm neu starten?")
    if eingabe == "ja":
        test_function()
    else:
        print("Das Programm wurde beendet")
 
 
def fehler_hinweis_zerodivision():
    print("Das teilen durch 0 ist nicht möglich")
 
 
def test_function():
    try:
        zahl1 = int(input("Bitte eine Zahl eingeben: "))
        zahl2 = int(input("Bitte zweite Zahl eingeben: "))
        ergebnis = zahl1 / zahl2
        print(ergebnis)
    except ValueError:
        fehler_hinweis()
    except ZeroDivisionError:
        fehler_hinweis_zerodivision()   # Mehrere Exceptions mit Errortypangabe untereinander für eine bessere Kontrolle
       
 
 
 
test_function()