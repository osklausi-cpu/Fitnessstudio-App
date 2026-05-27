test_Variablen1 = 10 #int
test_Variablen2 = "Das ist ein Satz" # string
test_Variablen3 = 1.9 # float
test_Variablen4 = True # boolean / bool

test_liste  = [10, 20, 30] # Liste vom Typ ist
test_liste2 = ["test1", "test2", "test3",] # Liste vom Typ string
test_liste3 = [1.4, 100.45, 45.46] #Liste vom Typ Float
test_liste4 = ["test1", 1.6, 10] # heterogene Liste (gemischte Datentyp Werte)

 #Python zählt von 0 auf 

 
""" Listen können bestimmte Funktionen benutzen die nur für Listen gedacht sind """
test_liste = [10, 20, 30]
test_liste[1] = 50 #ersezt index 1 mit 50
test_liste2 = ["string1", "string2", "string3"]


test_liste.append(80) # append hängt einen Wert an eine Liste hinten an
""" test_liste.extend(test_liste2) """ # extend hängt eine Liste an eine andere Liste dran, löst aber die angehängte Liste auf, das nur die Werte übernommen werden
""" test_liste.insert(2, "Wert eingefügt durch insert") """ # insert fügt an einem bestimmten Index einen Wert in eine Liste hinzu
""" test_liste.remove("Wert eingefügt durch insert") """ # remove entfernt den Eintrag mit dem Value den wir entferne möchten
test_liste.pop(1) # entfernt den Eintrag der ganz hinten in der Liste steht, bei indexangabe im Parameter entfernt man das Element an dem index
""" test_liste.clear() """ # deletes all entries in our list
test_liste.sort(reverse=True) # Sortiert eine Liste (reverse=True absteigend)
kopierte_liste = test_liste.copy() # kopiert eine vorhandene Liste
test_liste.count(10) # Zählt wie oft ein Wert in einer Liste vorhanden ist
 
 
print(test_liste)
print(kopierte_liste)
print(test_liste.count(10))

###########################################################################
#Buschtaben vergrößern

liste = ["a", "b", "c", "d" ]
for i in liste:
    print(i.upper())
    
# Erklärung:
# i ist jedes Element der Liste "a", "b", "c", "d".
# i.upper() wandelt den Buchstaben in Großbuchstaben um.
# print() gibt ihn aus.