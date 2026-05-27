
#Aufgaben:

# 1. Erstelle 5 Listen, wobei jeweils eine Liste nur strings, eine andere nur integer, eine weitere nur floats beinhaltet. Was in den anderen beiden steht ist egal

liste1 = ["Hallo wie geht's?", "Mir geht's gut.", "Und dir?"]     #String
liste2 = [1,2,3]                    #int
liste3 = [2.2, 2.3, 2.4]            #Float
liste4 = [True, False, True, False] #Boolean

from collections import deque
zahlen = deque([1, 2, 3, 4])        #deque
farben = ("rot", "grün", "blau")    #tuple

#Was ist deque?
# deque steht für “double-ended queue”, also doppelt-ended Schlange.Es ist eine spezielle Art von Liste, die schnell Elemente am Anfang und Ende hinzufügen oder entfernen kann.
# Mit einer normalen Liste geht das am Anfang langsam, weil Python alle Elemente verschieben muss.

#. Was ist ein Tupel? 
# Ein Tupel ist wie eine Liste, aber unveränderlich (immutable). Das heißt, du kannst keine Elemente hinzufügen,
# entfernen oder ändern. Tupel werden mit runden Klammern () geschrieben.

#Warum from collections import deque? 
# deque ist kein Standardtyp wie list oder int.
# Es ist Teil des Moduls collections, also eines Zusatzpakets in Python.
# Python weiß erst dann, was deque ist, wenn man es importiert.

# 2. Hänge 3 Werte an deine 1. Liste an
liste1.append("Wie geht's dir?")
liste1.append("Mir geht's gut")
liste1.append("Schön, dich zu sehen")

# 3. Nimm deine 2. Liste und hänge sie an deine erste Liste, lass sie dir danach ausgeben

liste1.extend(liste2)

# 4. Füge deinen Namen und 2 weitere Namen deiner Klassenkameraden deiner 1 Liste an Position 3, 4 und 6 hinzu

liste1.insert(2, "Osman")
liste1.insert(3, "Firat")
liste1.insert(5, "Maria")

# 5. Entferne einen Wert mit der Methode remove aus deiner 4. Liste. begründe warum der Wert trotzdem noch in der Liste vorhanden sein könnte.
liste4.remove(True)
#Erklärung warum der Wert trozdem in der Liste ist.
# remove() sucht von vorne nach hinten.
# Sobald es den Wert gefunden hat, wird er gelöscht.
# Danach hört Python auf – der Rest bleibt drin.

# 6. Werfe das letzte Element aus deiner 1. Liste raus.
liste1.pop()

#7. Lösche den Inhalt aus deiner 5. Liste und gib sie aus, um zu prüfen ob die Liste wirklich leer ist
zahlen.clear()

# 8. Sortiere deine 2 Liste absteigend und gib sie aus
liste2.sort(reverse=True)


#sort() sortiert die Liste aufsteigend standardmäßig.
# Mit reverse=True wird absteigend sortiert.
#liste.sort() → aufsteigend
#liste.sort(reverse=True) → absteigend


#9. Kopiere deine 4. Liste und lasse sie dir ausgeben mit dem Satz: "Das ist die Kopie von Liste 4"
Das_ist_die_Kopie_von_Liste_4 = liste4.copy()
print(Das_ist_die_Kopie_von_Liste_4)
#liste4.copy() Erstellt eine neue Liste, die die gleichen Elemente wie liste4 enthält. Die Original-Liste bleibt unverändert.

# 10. Füge einen Eintrag in deiner Kopie hinzu, lasse dir danach die Kopie und die original Liste ausgeben und schau ob das ändern der Kopie die echte Liste verändert hat.

Das_ist_die_Kopie_von_Liste_4.insert(True)
print(Das_ist_die_Kopie_von_Liste_4)
print(liste4)

# 11. Zähle wie oft der Name Alex in deiner 1. Liste vorhanden ist
liste1.count(alex)
print(liste1)

#
# 12. Zähle wie oft dein Name in der 1. Liste vorhanden ist
#
# 13. Prüfe wie oft die Zahl 3 in deiner 2. Liste ist
#
# 14. Sortiere die 3 Liste aufsteigend, weil diese sich sonst ausgeschlossen fühlt >;)