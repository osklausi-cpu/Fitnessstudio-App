# Eine einfache Funktion ohne Parameter
def test_funktion1():
    print("Hallo")
 
 
test_funktion1()
 
#####################################################################################

# Eine Funktion mit einem Parameter
 
 
def test_funktion2(parameter):  # im Parameter steht der Wert aus Funkitonsaufruf
    print(parameter)  # mit diesem Wert können wir in unserer Funktion weiter arbeiten
 
 
test_funktion2(10)  # es wird eine Zahl als Parameter übergeben
 
#####################################################################################
 
 
def test_funktion3(
    param1, param2
):  # Es können beliebig viele Parameter empfangen werden
    ergebnis = param1 + param2
    print(ergebnis)
 
 
test_funktion3(10, 20)  # Es können 2 Parameter mit beliebiegem Wert übergeben werden
 
 
# Wenn es mehr als 3 Parameter zu übergeben gibt, sollte ein Dicitonary übergeben werden
def test_funktion4(schueler):
    print(schueler["name"])
 
 
benutzer = {
    "name": "Mariia",
    "alter": 20,
    "kurs": "backend development",
    "preis": 3500,
    "kurslaufzeit": 130,
}
 
test_variable = {
    "name": "Udo",
    "alter": 65,
}
 
test_funktion4(test_variable)
test_funktion4(benutzer)
#####################################################################################
 
 
def test_funktion5(
    param1="Guten", param2="Tag"
):  # setzen der Parameter mit default werten
    print(f"{param1} {param2}")
 
 
test_funktion5(
    "Bonjour", "Je suis Jacques"
)  # default Werte werden überschrieben wenn Parameter übergeben werden
 
#####################################################################################
 
 
def test_funktion6(
    param1, param2
):  # Funktion mit return (Liefert dir direkt die Antwort zurück)
    ergebnis = param1 + param2
    return ergebnis  # Das Ergebnis wird direkt zurückgegeben und kann bei dem Aufruf verarbeitet werden
 
 
print(
    test_funktion6(15, 10)
)  # Hier wird das Ergebnis des returns in der print Anweisung weiterverarbeitet
 
######################################################################################
 
 
def test_funktion7(zahl1: int, zahl2: int) -> int:
    ergebnis = zahl1 + zahl2
    return ergebnis
 
 
print(test_funktion7(100, 200))