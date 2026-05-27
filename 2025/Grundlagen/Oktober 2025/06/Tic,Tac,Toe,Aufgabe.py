# Aufgabe 1
# erstelle mit einer List Comprehension 3 Listen mit einem Leerzeichen in einer Liste mit dem Namen Spielfeld
# gib deine List Comprehension aus
# die Ausgabe sollte so aussehen: [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
 
 
# Aufgabe 2
# 2.1 Suche im Internet nach der Methode .join() und erkläre im Detail was diese macht

# 1 .join() gehört zu Strings (Texten).
#   → Deshalb steht vor .join() immer etwas in Anführungszeichen.
# 2 Das, was vor .join() steht, ist das Trennzeichen.
# → Also das, was zwischen die Wörter gesetzt wird.
# Beispiel: " ".join(...) = Leerzeichen zwischen den Wörtern.
# ", ".join(...) = Komma und Leerzeichen dazwischen.
# 3 In die Klammern kommt eine Liste mit Texten.
# → z. B. ["Apfel", "Banane", "Kirsche"]
# 4 .join() verbindet alle Texte aus der Liste zu einem einzigen String.
# 5 Alle Elemente in der Liste müssen Texte (Strings) sein.
# → Wenn du Zahlen hast, musst du sie erst mit str() umwandeln.
# 6 .join() ist der richtige Weg, Texte zusammenzusetzen.
# → Es ist schneller und besser als viele + in einer Schleife.
# 7 .join() funktioniert so:
# "Trennzeichen".join(Liste)
# → Lies das wie:
# „Verbinde alle Wörter aus der Liste und setze Trennzeichen dazwischen.“


# 2.2 Schreibe eine Funktion mit dem Namen zeichne Spielfeld mit einer for Schleife, die jede Liste deiner List Comprehension untereinander ausgibt
# 2.3 Benutze die join Methode, um die Listen mit einem " | " Zeichen miteinander zu verbinden und gebe sie in der Console aus.
# 2.4 füge jeder Liste in einer Reihe einen Boden mit "-" hinzu und gebe dein Spielfeld in der Console aus. (Tipp: 9 Trennstriche sehen gut und symmetrisch aus)
# Dein Ergebnis sollte etwa wie folgt aussehen:
#
#  |   |
#---------
#  |   |
#---------
#  |   |
#---------
 
 
# Aufgabe 3
# 3.1 Baue eine Hauptfunktion mit dem Namen starte_spiel(), kopiere deine List Comprehension mit deinem
#     Spielfeld in die Funktion, so das dein Spielfeld bei dem Aufruf der Funktion erstellt wird
# 3.2 Definiere eine Variable mit dem Namen aktueller_spieler = 'X' in deiner Funkion
# 3.3 Baue eine While Schleife, in deiner starte_spiel() Funktion, die bei dem Start der Schleife
#     deine Funktion zeichne_spielfeld aufruft. (TIPP: Vergiss nicht die Parameterübergabe)
# 3.4 Fordere innerhalb deiner While Schleife eine Eingabe an, welche die Zeile mit einer Zahl empfängt und speichere den Wert der
#     Eingabe in der Variable zeile. Dieser Wert wird später auf den Index deines Feldes zugreifen
# 3.5 Fordere innerhalb deiner While Schleife eine weitere Eingabe an, welche die Spalte mit einem Zahlenwert empfängt, die später dem Index der
#     Spalte zugewiesen wird und speichere den Wert der Eingabe in einer Variablen mit dem Namen spalte
#      (TIPP: Aus der Kombination deiner Eingabe ergeben sich später die Indizes und somit die Stelle an der deine Wahl platziert wird)
 
 
# Aufgabe 4
# Du hast ein 2 Dimensionales Spielfeld gebaut, auf dessen Felder du zugreifen kannst. Finde heraus, wie du das Zeichen deines aktuellen Spielers
# auf die Felder der getätigten Eingabe setzen kannst und erweitere deine Funktion starte_spiel() mit der Zuweisung X auf die Eingabe des Spielers
 
 
# Aufgabe 5
# Wechsle den aktuellen Spieler in deiner While Schleife von "X" auf "O" und falls dieser Spieler schon auf "O" stehen sollte, wechsle ihn wieder zu "X"
# Teste mal aus, ob es schon funktioniert
 
 
# Aufgabe 6
# Atme mal tief durch, trink nen Schluck und wenn du fertig bist, zeige mit einem print Befehl an, welcher Spieler grade bei dem neuen Schleifendurchlauf an
# der Reihe ist.