kleines_paket = 7.99
mittleres_paket = 9.90
grosses_paket = 12.99
versandkosten = 1.99
rabatt = 1.25

eingabe_aufforderung = f"""Bitte waehlen Sie eines von 3 Paketen aus: 
        1: fuer das kleine Paket {kleines_paket}
        2: fuer das mittlere Paket {mittleres_paket:.2f}
        3: fuer das grosses Paket {grosses_paket}
""".replace(".",",")