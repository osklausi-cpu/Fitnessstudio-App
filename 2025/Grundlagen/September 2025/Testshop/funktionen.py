from variablen import*

def kontrolliere_eingabe(eingabe):
    if eingabe == 1: 
        gesamtpreis = kleines_paket + versandkosten
        preis_paket = str(f"{kleines_paket:.2f}").replace(".",",") 
        gesamtpreis = str(f"{gesamtpreis:.2f}").replace(".", ",") 
        print(f"Du hast dich fuer das kleine Paket entschieden für einen Preis von {preis_paket}€. Zusammen bezahlst du einen Gesamtpreis von {gesamtpreis} €")
    elif eingabe == 2:
        gesamtpreis = mittleres_paket + versandkosten
        preis_paket = str(f"{mittleres_paket:.2f}").replace(".",",") 
        gesamtpreis = str(f"{gesamtpreis:.2f}").replace(".",",")
        print (f"Du hast dich fuer das mittlere Paket entschieden für einen Preis von {preis_paket}€ Zusammen bezahlst du einen Gesamtpreis von {gesamtpreis} € ")
    elif eingabe == 3:
        gesamtpreis = grosses_paket - rabatt
        preis_paket = str(f"{grosses_paket:.2f}").replace(".",",") 
        gesamtpreis = str(f"{gesamtpreis:.2f}").replace(".",",")
        print (f"Du hast dich fuer das grosse paket entschieden Für einen Preis von {preis_paket}€ Zusammen bezahlst du einen Gesamtpreis von {gesamtpreis} € ")

        # scope= gültigkeitsbereich
        # Variablen = einfacher datentyp taschen
        # float = kommazahl
        # string= text
        # 