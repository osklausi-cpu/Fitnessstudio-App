# Aufgabe 7
# Finde die Tiere, die nur in einem der beiden Gehege vorkommen (nicht in beiden).
 
gehege_1 = {"Löwe", "Tiger", "Elefant", "Zebra"}
gehege_2 = {"Tiger", "Elefant", "Giraffe", "Nashorn"}

tiere = gehege_1.symmetric_difference(gehege_2)
print(tiere)


