liste1 = [10, 20, 30, 40, 50]
liste2 = ["string1", "string2", "string3", "string4"]
liste3 = [1.5, 2.5, 10.7, 100.5]


# Prozedur erstellen (Funktion die immer wiederkehrende Aufgaben erledigt)
def rechts_verschieben(liste):
    letztes_element = liste[-1]
    rest_elemente = liste[:-1]
    neue_liste = []
    neue_liste.append(letztes_element)
    neue_liste.extend(rest_elemente)

    print(
        neue_liste
    )  # soll nur unsere Kontrolle die ANzeigt ob wir auch die richtigen Werte speichern


rechts_verschieben(liste1)
