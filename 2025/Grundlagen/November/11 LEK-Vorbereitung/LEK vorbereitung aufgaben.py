#Aufgabe 3
# schreibe eine Funktion mit dem Namen funktion3, welche die Parameter aus dem Funktionsaufruf empfängt, addiert und ausgibt
 
def funktion3(a,b):
    return a + b
   
ergebnis = funktion3(100, 200)
print(ergebnis)

# Aufgabe 4
# schreibe eine Funktion mit dem Namen funktion4, welche einen Rückgabewert ausgibt welcher durch die Variablen a + b berechnet wird
 
def funktion4(a,b):
    return a + b 

lösung = funktion4(2,2)
print(lösung)

# Aufgabe 5
#
#
# schreibe eine Funktion mit dem namen funktion5, welche 2 parameter empfängt.
# Diese werden wie folgt in der Funktion berechnet: (parameter1 + parameter2) / 2
# Gib dein Ergebnis als Rückgabewert aus

def funktion5(a,b):
    return (a + b) /2

lösung = funktion5(6+2)
print(lösung)

#Aufgabe 6
#
# Warum funktioniert folgende Funktion nicht ? Begründe es und finde eine Lösung
 
def ups_das_klappt_nicht(a, b):
    c = a * b
    return c
 
ergebnis = ups_das_klappt_nicht(2,2)
print(ergebnis)

#Aufgabe 7
# Was gibt folgende Funktion aus? Beschreibe was passiert
 
def funktion7():  #Funktion ohne Parameter gibt 10 zurück wenn aufgerufen.
    return 10
 
x = 100 + funktion7()
print(x)

# Die funktion gibt 110 aus, da 10 returnt werden und x = 100+10


# Was ist eine rekursive Funktion ? 
 
def rekursive_funktion(x, y):
    if x == 0:
        return 0
    else:
       print(f"Hier ist die Zahl x: {x}, Und hier ist y: {y}")
       return y + rekursive_funktion(x-1, y) # bei jeden Aufruf der Funktion selbst, wird x um ein veringert
 
print(rekursive_funktion(3, 4))





# Aufgaben Rechenoperatoren

#Aufgabe 1
# Deklariere Variablen der folgenden primitiven Datentypen und weise passende Werte zu und gib sie aus:
# int, float, str, bool

# Ganze Zahl int
alter = 25
# Kommazahl float
menge = 2.5
# text str
name = "Anna"
#boolean
ist_student = True

print(alter, menge, name, ist_student)

# Aufgabe 2
# Schreibe ein Programm, das zwei Ganzzahlen als Eingabe annimmt und folgende Berechnungen durchführt:
# Addition, Subtraktion, Multiplikation, division, modulo
 
zahl1 = int(input("Geben Sie erste Zahl ein: "))
zahl2 = int(input("Bitte zweite Zahl eingeben :"))

def rechnen(a, b):
    print("Addition: ", a + b)
    print("Subtraktion: ", a - b)
    print("Multiplikation: ", a * b)
    if b != 0:
        print("Division: ", a / b)
        print("Modulo: ", a % b)
    else:
        print("Division und Modulo nicht möglich (b = 0).")

rechnen(zahl1, zahl2)

# Aufgabe 3
# Schreibe ein Programm, welches einen Fließkommazahl als Input annimmt und diesen Wert in einen Integer umwandelt.
# Danach soll das Programm prüfen ob der Integer Wert grade oder ungrade ist.

kommazahl = float(input("Zahl bitte: "))

intWert = int(kommazahl)

if intWert % 2 == 0:
    print("gerade")
else:
    print("ungerade")


# Aufgabe 4
# Schreibe ein Programm, welches das Alter einer Person abfragt und prüft, ob die Person volljährig ist oder nicht.
# Gib eine entsprechende Nachricht aus, ob Lina, die grade 14 geworden ist in die Discothek darf (Eintritt ab 18)
alterKontrolle = int(input("wie alt bist du?: "))

if alterKontrolle < 18:
    print("sorry zu jung")
else:
    print("Gerne rein")


 
# Aufgabe 5
# Schreibe ein Programm, das drei Zahlen als Input entgegen nimmt und prüft, welche davon die größte ist.
# Gib die größte Zahl aus
zahl1 = int(input("geben sie die erste Zahl ein: "))
zahl2 = int(input("geben sie die zweite Zahl ein: "))
zahl3 = int(input("geben sie die dritte Zahl ein: "))

groesteZahl = max(zahl1, zahl2, zahl3)
print(f"Groeste zahl ist {groesteZahl}")
 
# Aufgabe 6
# Schreibe ein Programm, das zwei Ganzzahlen vergleicht und ausgibt, ob sie gleich sind, oder ob eine Zahl größer
# oder kleiner als die andere ist.

zahl1 = int(input("Bitte erste Zahl: "))
zahl2 = int(input("Bitte zweite Zahl: "))

if zahl1 == zahl2:
    print("Zahl 1 und Zahl 2 sind gleich")

elif zahl1 > zahl2:
    print("Zahl 1 ist größer")

else:
    print("zahl 2 ist größer")

 

# Aufgabe 7
# Schreibe ein Programm welches prüft, ob eine Person Zugang zu einem System erhält.
# Die Person hat entweder die Rolle Admin oder Superuser oder das Passwort "secret" um auf das System zugreifen zu können
# Ansonsten wird der Zugriff verweigert
# benutze or

zugangErlauben = input("Was für eine Rolle haben Sie oder nennen Sie das Passwort: ")

if zugangErlauben == zugangErlauben == "Admin" or zugangErlauben == "Superuser" or zugangErlauben == "secret":
    print("herzlich willkomen")
else:
    print("Zugriff verweigert")

 
 
# Aufgabe 8
# Schreibe eine Funktion, die überprüft, ob eine gegebene Zahl sowohl größer als 10 als auch kleiner als 20 ist.
#  Verwende dafür bitte den and Operator und einen Input der eine Eingabe entgegen nimmt.
 
 
# Aufgabe 9
# Schreibe eine Funktion, die überprüft, ob eine Zahl entweder kleiner als 0 oder
# größer als 100 ist. Verwende dabei den or Operator und einen Input für eine Eingabe
 
 
# Aufgabe 10 Sonderaufgabe
# Schreibe ein Programm, das ein Passwort von einem Nutzer entgegen nimmt und überprüft
# ob es mindestens 8 Zeichen lang ist und es muss entweder eine Zahl oder ein Sonderzeichen (@, #, $, %) enthalten

