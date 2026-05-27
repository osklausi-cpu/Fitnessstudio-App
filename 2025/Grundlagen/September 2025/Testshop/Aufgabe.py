#Baue heute mindestens 3 if else Verzweigungen wie aus dem Unterricht nach. 
 
#Das selbe nochmal mit mindestens 1 if elif und else Struktur 


# 1. Alter
age = int(input("Bitte gebe dein Alter ein: "))

if age < 18:
    print("Achtung, der Nutzer ist jünger als 18")
elif age == 18:
    print("Der Nutzer ist exakt 18")
else:
    print("Du bist volljährig")


# 2. Größe
groesse = float(input("Bitte gib deine Groesse in Metern ein: "))

if groesse < 1.80:
    print("Du bist zu klein")
else:
    print("Du bist groß genug")


# 3. Wasser
water = input("Ist das Wasser heute warm genug zum Schwimmen? (ja/nein) ")

if water.strip().lower() == "ja":
    print("Sehr gut.")
else:
    print("Schade, hatte schon Hoffnung.")

#.strip() entfernt alle Leerzeichen am Anfang und Ende. 
# Beispiel: " ja " → "ja"
# .lower() wandelt alle Buchstaben in Kleinbuchstaben um.
# Beispiel: "Ja" → "ja"

# 4. Lieferzeit
frage = "Wie lange braucht der Lieferservice? (in Minuten) "
eingabe = int(input(frage))

if eingabe == 10:
    print("Der Lieferservice ist sehr schnell")
else:
    print("Der Lieferservice ist langsam")
