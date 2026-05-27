# Aufgabe 2

# 2.1: Die Methode .join()

# Die Methode .join() ist eine String-Methode in Python, die verwendet wird, um

# eine Sequenz (z. B. Liste oder Tuple) von Strings zu einem einzigen String zu verbinden.

# Dabei wird der String, auf dem .join() aufgerufen wird, als Trennzeichen zwischen

# den Elementen eingefügt.

#

# Beispiel:

# ", ".join(["Apfel", "Banane", "Kirsche"])

# ergibt: "Apfel, Banane, Kirsche"
 
# 2.2: Spielfeld mit List Comprehension








SF = [[' ' for _ in range(3)] for _ in range(3)]  # 3x3 Spielfeld mit Leerzeichen
 
# Funktion, die jede Liste untereinander ausgibt (roh)

def SF_roh(spielfeld):

    for reihe in spielfeld:

        print(reihe)
 
# 2.3: Funktion, die join benutzt, um die Elemente mit " | " zu verbinden

def SF_join(spielfeld):

    for reihe in spielfeld:

        print(" | ".join(reihe))
 
# 2.4: Funktion, die nach jeder Reihe einen Boden von 9 Trennstrichen ausgibt

def SF_boden(spielfeld):

    trennstrich = "-" * 9  # 9 Trennstriche

    for i, reihe in enumerate(spielfeld):

        print(" " + " | ".join(reihe))

        # Trennstrich nur zwischen den Reihen, nicht nach der letzten

        if i < len(spielfeld) - 1:

            print(trennstrich)
 
# --- Beispiel: alle Funktionen ausführen ---











if __name__ == "__main__":

    print("Rohes Ausgeben der Zeilen (2.2):")

    SF_roh(SF)

    print("\nMit join (2.3):")

    SF_join(SF)

    print("\nMit Boden (2.4):")

    SF_boden(SF)

 