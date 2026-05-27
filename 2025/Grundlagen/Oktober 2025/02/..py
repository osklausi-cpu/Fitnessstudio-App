namens_liste = ["Ilka", "Oliver", "Sascha", "Johannes", "Katja", "Firat", "Michael"]
 
""" for name in namens_liste:
    print(name) """
 
# einfache Iteration durch eine Liste welche alle Namen aus der Liste ausgibt
 
###########################################################################################
 
 
""" for index in range(len(namens_liste)):
    if namens_liste[index] == "Oliver":
        print("Oliver ist vorhanden") """
 
# range() bestimmt einen Zahlenbereich, wie oft durch die Schleife iteriert werden soll
# len() gibt eine ganze Zahl in Form eines Integers zurück. In unserem Fall ist das die Anzahl der Elemente in unserer Liste
 
#############################################################################################
 
 
####################################### WHILE SCHLEIFE ##########################################
 
 
while True: # Schleife wird beendet wenn der Zähler die Zahl 10 erreicht
    eingabe = int(input("Bitte etwas eingeben: "))
    if eingabe == 0:
        print("Die While Schleife wurde beendet!!!")
        break  # break unterbricht und verlässt die While Schleife
    elif eingabe == 15:
        print("Es wurde die 15 eingegeben, wir springen zum Anfang der Schleife!")
        continue # continue springt wieder an den Anfang der Schleife zurück
    elif eingabe == 100:
        print("100 eingegeben!!!")
    else:
        print("Irgendwas anderes!!!")
 
 
zaehler = 0
while zaehler <= 10: # Schleife wird beendet wenn der Zähler die Zahl 10 erreicht
    eingabe = int(input("Bitte etwas eingeben: "))
    if eingabe == 0:
        print("Die While Schleife wurde beendet!!!")
        break  # break unterbricht und verlässt die While Schleife
    elif eingabe == 15:
        print("Es wurde die 15 eingegeben, wir springen zum Anfang der Schleife!")
        continue # continue springt wieder an den Anfang der Schleife zurück
    elif eingabe == 100:
        print("100 eingegeben!!!")
        print(zaehler)
    else:
        print("Irgendwas anderes!!!")
 
    zaehler += 1