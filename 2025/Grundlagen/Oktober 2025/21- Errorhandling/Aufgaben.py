# Aufgabe 1
# Schreibe ein Programm, das den Benutzer auffordert, eine ganze Zahl einzugeben und diese Zahl verdoppelt.
# Verwende deine Kenntnisse im Error Handling um eine ValueError exception abzufangen, falls der Benutzer
# etwas anderes als eine Zahl eingibt.

try:
    zahl = int(input("Geben Sie eine Zahl ein: "))
    ergebnis = zahl * 2
    print("Das Doppelte Ihrer Zahl ist:", ergebnis)

    
except ValueError:
    print("Fehler: Bitte geben sie eine gültige ganze Zahl ein!")

# In Python dient try dazu, Codeblöcke zu markieren, bei denen ein Fehler auftreten könnte.
# Alles, was in den try-Block geschrieben wird, wird "versucht" auszuführen. Wenn ein Fehler 
# auftritt, springt Python automatisch in den passenden except-Block.

 
# Aufgabe 2

# Schreibe eine Funktion mit dem Namen addieren(a, b), die zwei Zahlen als Parameter empfängt.
# Verwende deine Error Handling Skills um einen TypeError abzufangen, falls einer der Parameter
# kein Zahlentyp ist

def addiere(a, b):
    try:
       ergebnis = a + b
       return ergebnis
    except TypeError:
        print("Fehler: Beide Parameter müssen Zahlen sein!")



# Aufgabe 3
# Schreibe eine Funktion mit dem Namen teilen, die 2 Zahlen als Parameter erhält und das Ergebnis einer
# Division zurück gibt. Verwende try und except um eine Division durch Null zu verhindern und eine
# entsprechende Fehlermeldung auszugeben

def teilen(a, b):
    try:
        ergebnis = a / b
        return ergebnis
    except ZeroDivisionError: #„Du hast versucht, etwas zu teilen, was mathematisch nicht geht.“
        print("Fehler: Division durch Null ist nicht erlaubt")
        return None  # und die Funktion gibt None zurück (statt z. B. abzustürzen).
    

# „Falls genau dieser Fehler (Division durch Null) auftritt — bitte stürze nicht ab, 
# sondern führe meinen Code im except-Block aus.“
 
 
# Aufgabe 4
# Du findest eine Liste mit 5 Zahlen. Der Benutzer soll einen Index eingeben
# und das Programm gibt das Element an dieser Position aus. Verwende Error Handling um einen
# IndexError und einen ValueError abzufangen wenn der Benutzer keinen gültigen Index eingibt
# (Am liebsten durch eine seperate exception)
 
numbers = [10, 20, 30, 40, 50]

try:
    eingabe = int(input("Index eingeben bitte (0-4): "))
    print("Das Element an dieser Position ist: ", numbers[eingabe])

except ValueError:
    print("Fehler: Bitte gib eine ganze Zahl ein!")

except IndexError:
    print ("Fehler: Dieser Index existiert nicht! (gültig: 0 bis 4)")

# Was passiert hier:
# Der Benutzer gibt etwas ein.
# int(input(...)) kann einen ValueError werfen, wenn der Text keine Zahl ist.
# numbers[eingabe] kann einen IndexError werfen, wenn der Index außerhalb der Liste liegt.
# Jeder Fehler wird separat behandelt mit einer passenden Fehlermeldung.
 
# Aufgabe 5
# Wenn der Benutzer einen Namen eingibt, der nicht im Dictionary existiert, soll eine Meldung
# "Fehler: Name nicht gefunden!" ausgegeben werden. Verwende KeyError.
 
mitarbeiter = {
    "Daniel": 25,
    "Lukas": 30,
    "Serhat": 15,
    "Georg": 66,
    "Mandy": 11,
}

try:
    name = input("Bitte geben Sie einen Namen ein: ")
    print("Alter:", mitarbeiter[name]) #Python versucht mitarbeiter[name] → greift auf den Wert im Dictionary zu.

except KeyError:
    print("Dieser Name exsistiert nicht")


#Erst Zugriff auf Dictionary kann KeyError auslösen:
#Ein KeyError ist immer mit Dictionaries in Python verbunden.

# Aufgabe 6
# Schreibe ein Programm, dass eine Datei mit dem Namen rechnung.txt öffnet und deren Inhalt auf dem Bildschirm ausgibt
# Erstelle einen Ordner mit dem Namen dateien. Speichere darin eine Datei namens rechnung.txt und finde heraus wie du die Datei öffnen und in der Print ausgabe lesen kannst.
# Verwende FileNotFoundError wenn die Datei nicht existiert.  

try:
    #Datei öffnen
    with open("Oktober 2025/21- Errorhandling/dateien/rechnung.txt" ,"r") as datei:
        inhalt = datei.read() #gesamten Inhalt lesen
        print(inhalt)         # ausgeben

except FileNotFoundError:
    print("Fehler: Die Datei wurde nicht gefunden!")

# try bedeutet: „Versuche diesen Code auszuführen, aber sei vorbereitet auf Fehler“.
# Wenn ein Fehler passiert, wird der normale Programmablauf unterbrochen 
# und Python springt zum passenden except-Block.

# open() → öffnet eine Datei
# Erster Parameter: Pfad zur Datei "Oktober 2025/21- Errorhandling/dateien/rechnung.txt"
# Zweiter Parameter: "r" → read mode, Datei wird nur gelesen
# with = „öffne die Datei und kümmere dich automatisch um das Schließen“
# ohne with = „du musst selbst auf das Schließen achten“ datei.close()
 
# Aufgabe 7
# Schreibe ein Programm, welches eine Datei mit dem Namen Test in deinem Ordner dateien speichert und schreibe eine kleine Geschichte dort hinein.
# Finde heraus, welcher Modus für das schreiben von Dateien genutzt werden kann.
# Was wäre ein alternativer Modus, wenn du etwas an die Datei anhängen willst ohne die Datei bei dem erneuten ausführen zu überschreiben?
 
def programm():
    # Pfad zur Datei
    datei_pfad = "Oktober 2025/21- Errorhandling/dateien/Test.txt"
    
    # Geschichte, die in die Datei geschrieben wird
    geschichte = """Es war einmal ein kleiner Drache, der im Wald lebte.
Er liebte es, Abenteuer zu erleben und neue Freunde zu finden.
Eines Tages entdeckte er einen geheimen See, der im Mondlicht funkelte."""
    
    # Datei öffnen im Schreibmodus "w" (überschreibt bei erneutem Ausführen)
    with open(datei_pfad, "w", encoding="utf-8") as datei:
        datei.write(geschichte)

    print("Die Geschichte wurde erfolgreich in die Datei geschrieben!")

# Programm ausführen
programm()

# Aufgabe 8
# Schreibe ein Programm, das die Variable namens zahl verwendet und diese mit einem Wert von 10 Multipliziert.
# Verwende Error Handling um einen NameError abzufangen, für den Fall, das die Variable nicht definiert wurde.

try:
    ergebnis = zahl * 10
    print("Ergebnis ist: ", ergebnis)
except NameError:
    print("Fehler: Die Variable 'zahl' wurde nicht definiert")

# try: → Der Code in diesem Block wird versucht auszuführen.
# ergebnis = zahl * 10 → Hier wird angenommen, dass zahl existiert.
# Wenn zahl nicht definiert ist, löst Python einen NameError aus.
# except NameError: → Fängt diesen Fehler ab und gibt eine entsprechende Fehlermeldung aus.

 
 
# Aufgabe 9
# Schreibe ein Programm, das eine einfache Benutzerverwaltung in einem Dictionary simuliert.
# Frage den Benutzer ob er sich anmelden, Registrieren oder das Programm beenden möchte.
# Eine Registrierung wird in einem Dictionary gespiechert mit einem Namen und dem Alter
# Fange folgende Fehler ab: Der Name darf nicht leer sein und das Alter muss eine ganze Zahl sein.
# Wenn der Benutzer sich anmelden möchte, muss er nur seinen Namen eingeben.
# Wenn der Benutzer im Dicitonary vorhanden ist, gib seinen Namen und sein Alter aus.
# Wenn der Benutzer nicht im Dictionary gefunden wird, wird eine Fehlermeldung angezeigt durch einen KeyError.