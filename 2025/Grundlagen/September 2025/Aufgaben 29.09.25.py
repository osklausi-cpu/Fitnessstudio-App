 
# Aufgabe 1
# Deklariere Variablen der folgenden primitiven Datentypen und weise passende Werte zu und gib sie aus:
# int, float, str, bool
zahl_int = 29   
float = 2.23
text = "Heute ist ein schöner Tag"
wahrheitswert_bool = True

print(zahl_int)
print(float)
print(text)
print("bool:", wahrheitswert_bool)


# Aufgabe 2
# Schreibe ein Programm, das zwei Ganzzahlen als Eingabe annimmt und folgende Berechnungen durchführt:
# Addition, Subtraktion, Multiplikation, division, modulo

#Bei Divisionen und Modulo muss man aufpassen, wenn die zweite Zahl 0 ist
# if zahl2 !=0: 👉 „Wenn die zweite Zahl NICHT 0 ist …“ 
#Warum brauchen wir das?
# Teilen durch 0 ist verboten (in Mathe und im Computer).
# Deshalb prüfen wir erst:
# Falls zahl2 nicht 0 → dann dürfen wir teilen und Modulo rechnen.
# Falls zahl2 0 → Ausgabe: „geht nicht“.

zahl1 = int(input("Geben Sie erste Zahl ein."))
zahl2 = int(input("Geben Sie die zweite Zahl ein"))

print(zahl1 + zahl2)
print(zahl1 - zahl2)
print(zahl1 * zahl2)

if zahl2 !=0:
    print("Division:", zahl1 / zahl2)
    print("Modulo", zahl1 % zahl2)
else:
    print("Division: nicht möglich (durch 0 teile geht nicht)")
    print("Modulo: nicht möglich (durch 0 teilen geht nicht)")

 
# Aufgabe 3
# Schreibe ein Programm, welches einen Fließkommazahl als Input annimmt und diesen Wert in einen Integer umwandelt.
# Danach soll das Programm prüfen ob der Integer Wert grade oder ungrade ist.

kommazahl =float(input("Geben Sie eine Kommazahl ein"))
ganzzahl = int(kommazahl)

if ganzzahl % 2 == 0:
    print(f"Die Zahl ist gerade{ganzzahl}")
else:
    print(f"Die Zahl ist ungerade{ganzzahl}")


# Aufgabe 4
# Schreibe ein Programm, welches das Alter einer Person abfragt und prüft, ob die Person volljährig ist oder nicht.
# Gib eine entsprechende Nachricht aus, ob Lina, die grade 14 geworden ist in die Discothek darf (Eintritt ab 18)

alter = int(input("Wie alt sind Sie?"))
if alter >= 18:
    print("Sie sind über 18, Sie dürfen rein kommen.")
else:
    print("Sie sind unter 18, bleiben Sie vor der Tür!")
 
 
# Aufgabe 5
# Schreibe ein Programm, das drei Zahlen als Input entgegen nimmt und prüft, welche davon die größte ist.
# Gib die größte Zahl aus
zahl1 = int(input("Geben Sie eine Zahl ein"))
zahl2 = int(input("Geben Sie eine Zahl ein"))
zahl3 = int(input("Geben Sie eine Zahl ein"))

groeste = max(zahl1, zahl2, zahl3)
print(groeste)

 
# Aufgabe 6
# Schreibe ein Programm, das zwei Ganzzahlen vergleicht und ausgibt, ob sie gleich sind, oder ob eine Zahl größer
# oder kleiner als die andere ist.
ganzzahl1 = int(input("Geben sie die erste Zahl ein"))
ganzzahl2 = int(input("Bitte die zweite Zahl"))

if ganzzahl1 == ganzzahl2:
    print("Die Zahlen sind gleich.")
elif ganzzahl1 < ganzzahl2 :
    print("Die erste Zahl ist kleiner.")

else:
    print("Die erste Zahl ist größer als die zweite Zahl.")

# Aufgabe 7
# Schreibe ein Programm welches prüft, ob eine Person Zugang zu einem System erhält.
# Die Person hat entweder die Rolle Admin oder Superuser oder das Passwort "secret" um auf das System zugreifen zu können
# Ansonsten wird der Zugriff verweigert
# benutze or
# Eingabe der Daten
rolle = input("Bitte geben Sie Ihre Rolle ein (Admin, Superuser, Benutzer): ")
password = input(("Bitte geben Sie ihr Passwort ein"))

if rolle == "Admin" or "Superuser" or password == "secret":
    print("Zugriff erlaubt")
else:
    print("Zugriff verweigert")

# Aufgabe 8
# Schreibe eine Funktion, die überprüft, ob eine gegebene Zahl sowohl größer als 10 als auch kleiner als 20 ist.
#  Verwende dafür bitte den and Operator und einen Input der eine Eingabe entgegen nimmt.
def pruefe_zahl(zahl):
    if zahl > 10 and zahl < 20:
        return True
    else:
        return False
# Eingabe von der Benutzerin/dem Benutzer
eingabe = int(input("Bitte geben Sie eine Zahl ein: "))

# Überprüfung der Zahl
if pruefe_zahl(eingabe):
    print("Die Zahl liegt zwischen 10 und 20.")
else:
    print("Die Zahl liegt nicht zwischen 10 und 20.")
 
# Aufgabe 9
# Schreibe eine Funktion, die überprüft, ob eine Zahl entweder kleiner als 0 oder
# größer als 100 ist. Verwende dabei den or Operator und einen Input für eine Eingabe


# Aufgabe 10 Sonderaufgabe
# Schreibe ein Programm, das ein Passwort von einem Nutzer entgegen nimmt und überprüft
# ob es mindestens 8 Zeichen lang ist und es muss entweder eine Zahl oder ein Sonderzeichen (@, #, $, %) enthalten
 











