# Aufgabe 1
# List Comprehension, um ein 3x3 Spielfeld zu erstellen
Spielfeld = [[' ' for _ in range(3)] for _ in range(3)]
print(Spielfeld)  # Ausgabe: [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Aufgabe 2
# 2.2-2.4: Funktion, die das Spielfeld zeichnet
def zeichne_spielfeld(feld):
    for reihe in feld:
        print(" | ".join(reihe))  # verbindet die Felder mit " | "
        print("-" * 9)  # Boden zwischen den Reihen

# Aufgabe 3-6: Hauptspiel-Funktion
def starte_spiel():
    # Spielfeld erstellen
    spielfeld = [[' ' for _ in range(3)] for _ in range(3)]
    aktueller_spieler = 'X'
    
    while True:           
        # Zeige den aktuellen Spieler
        print(f"Aktueller Spieler: {aktueller_spieler}")
        
        # Spielfeld ausgeben
        zeichne_spielfeld(spielfeld)
        
        # Spieler-Eingabe
        zeile = int(input("Gib die Zeile ein (0-2): "))
        spalte = int(input("Gib die Spalte ein (0-2): "))
        
        # Setze das Zeichen des Spielers auf das Feld
        if spielfeld[zeile][spalte] == ' ':
            spielfeld[zeile][spalte] = aktueller_spieler
        else:
            print("Dieses Feld ist schon belegt! Wähle ein anderes.")
            continue  # Schleife neu starten, ohne Spieler zu wechseln
        
        # Spieler wechseln
        if aktueller_spieler == 'X':
            aktueller_spieler = 'O'
        else:
            aktueller_spieler = 'X'

# Spiel starten
starte_spiel()
