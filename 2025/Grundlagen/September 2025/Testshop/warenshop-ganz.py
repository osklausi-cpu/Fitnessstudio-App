# Paketpreise und weitere Variablen
kleines_paket = 7.99
mittleres_paket = 9.90
grosses_paket = 12.99
versandkosten = 1.99
rabatt = 1.25

# Eingabeaufforderung
eingabe_aufforderung = f"""Bitte wählen Sie eines von 3 Paketen aus: 
    1: für das kleine Paket {kleines_paket:.2f}€
    2: für das mittlere Paket {mittleres_paket:.2f}€
    3: für das große Paket {grosses_paket:.2f}€
"""

# Funktion zur Eingabeprüfung
def kontrolliere_eingabe(eingabe):           #???
    if eingabe == 1:
        gesamtpreis = kleines_paket + versandkosten
        print(f"Du hast dich für das kleine Paket entschieden für einen Preis von {kleines_paket:.2f}€. "
              f"Zusammen bezahlst du {gesamtpreis:.2f}€.")

    elif eingabe == 2:
        gesamtpreis = mittleres_paket + versandkosten
        print(f"Du hast dich für das mittlere Paket entschieden für einen Preis von {mittleres_paket:.2f}€. "
              f"Zusammen bezahlst du {gesamtpreis:.2f}€.")

    elif eingabe == 3:
        gesamtpreis = grosses_paket - rabatt + versandkosten
        print(f"Du hast dich für das große Paket entschieden für einen Preis von {grosses_paket:.2f}€. "
              f"Nach Rabatt und Versandkosten bezahlst du {gesamtpreis:.2f}€.")

    else:
        print("❌ Ungültige Eingabe! Bitte 1, 2 oder 3 eingeben.")

# Hauptprogramm
eingabe = input(eingabe_aufforderung + "\n> ")

try:
    eingabe = int(eingabe)
    kontrolliere_eingabe(eingabe)
except ValueError:
    print("❌ Bitte eine Zahl eingeben (1, 2 oder 3).")
