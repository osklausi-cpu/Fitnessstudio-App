set1 = { 1,2,3,4,5 }
set2 = set([4,5,6])
 
############################## Methoden für Sets #############################################
set1.add(10) # fügt einen Wert einem Set hinzu
set1.remove(3) # remove löscht einen Wert aus einem Set
set1.discard(30) # hat den Vortei lwie bei remove das etwas gelöscht wird, wirft aber keinen Fehler wenn das Element nicht vorhanden ist.
ergebnis = set1.union(set2) # vereinigt zwei Sets miteinander
schnittmenge = set1.intersection(set2) # liefert eine Schnittmenge die beide gemeinsam haben
differenz = set1.difference(set2) # differenz bildet ein Set welches die Werte aus dem anderen subtrahiert.
 
print(set1)
print(set2)
print(ergebnis)
print(schnittmenge)
print(differenz)


# Grundlagen: Was ist ein Set?
# Ein Set (Menge) in Python ist eine Sammlung einzigartiger Elemente:
# Keine doppelten Werte
# Reihenfolge ist nicht garantiert
# Sehr effizient bei mathematischen Mengenoperationen (Vereinigung, Schnitt, Differenz etc.)