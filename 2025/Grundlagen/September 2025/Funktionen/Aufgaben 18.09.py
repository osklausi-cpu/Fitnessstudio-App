#Aufgabe 1
def funktion1(name):
    print(f"Hallo, hier ist {name}")

funktion1("Osman")
funktion1("bubi")

# Rufe funktion1 auf und übergebe ihr einen Namen

#Aufgabe 2
# Rufe funktion2 auf und ergänze sie mit einem sinnvollen parameter der übergeben wird, der berechnet werden kann
def funktion2(a):
    c = a + 10
    print(c)
 
funktion2(2)
 
 #Aufgabe 3
# schreibe eine Funktion mit dem Namen funktion3, welche die Parameter aus dem Funktionsaufruf empfängt, addiert und ausgibt

def funktion3(a, b):
    c = a + b
    print(c)
 
funktion3(100, 200)

# Aufgabe 4
# schreibe eine Funktion mit dem Namen funktion4, welche einen Rückgabewert ausgibt welcher durch die Variablen a + b berechnet wird

def funktion4(a, b):
    return a + b  
lösung = funktion4(2, 5)

print(lösung)

# Aufgabe 5
#
#
# schreibe eine Funktion mit dem namen funktion5, welche 2 parameter empfängt.
# Diese werden wie folgt in der Funktion berechnet: (parameter1 + parameter2) / 2
# Gib dein Ergebnis als Rückgabewert aus

def funktion5(parameter1, parameter2):
    return (parameter1+parameter2)/2

ergebnis=funktion5(2, 6)

print(ergebnis) 

#Aufgabe 6
#
# Warum funktioniert folgende Funktion nicht ? Begründe es und finde eine Lösung
 
def ups_das_klappt_nicht(a, b):
    c = a * b
    return c
 
ergebnis = ups_das_klappt_nicht(2, 3)
print(ergebnis)
# Weil es die Werte im Zeile 58 fehlen
 
#Aufgabe 7
# Was gibt folgende Funktion aus? Beschreibe was passiert
 
def funktion7():
    return 10
 
x = 100 + funktion7()

print(x)

# Die Funktion gibt 110 aus, da x=100+10
 
 
# HIHIHIIHIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII HAAAHAHAHAHAHAAAAAA WUAAAAAHAHAHAHAAHAHAHAHAHAHAH  ;)