product = {
    "id": 12345,
    "name": "Fernseher",
    "preis": 499.99
}
# Hier gilt:

# {} zeigt: Das ist ein Dictionary
# Schlüssel (z. B. "name") steht links
# Wert (z. B. "Anna") steht rechts
# Dazwischen steht ein Doppelpunkt (:)
# Mehrere Paare werden mit Kommas getrennt

 
############################################ Zugriff auf die Werte eines Dictionaries ############################
print(product["name"])
print(product["preis"]) # direkter Zugriff auf die Keys eines Dicitonaries
product["testkey"] = "Das ist ein Test" # direktes erstellen eines Key Value Paares
# print(product['abc']) # Würde einen Fehler werfen, weil der Key abc nicht im Dictionary existiert
print(product.get('abc')) # Sichere Methode um auf einen Key zuzugreifen, gibt None zurück wenn der Key nicht existiert
 
if product.get('abc') == None:       # Prüft ob ein Zugriff auf einen Key None zurück gibt. (Nur bei verwendung von get())
    print("Der Key Abc existiert nicht")

     
 
############################################  Grund Funktionen für Dictionaries ###################################
 
print(product.keys()) # iteriert in einem Dictionary über alle Keys und gibt sie als Liste aus
print(product.values()) # iteriert in einem Dicitonary über alle Values und gibt sie als Liste aus
print(product.items()) # iteriert in einem Dictionary über alle Key Value Paare und gibt sie in einer Liste als Tupel Paare zurück
 
############################################ Weitere Methoden für Dictionaries ####################################
 
product.update({"preis":289.98}) # update updated in diesem Fall ein bestehendes Key Value Paar
product.update({"anzahl": 100}) # In diesem Fall wird ein neues Key Value Paar erzeugt, wenn es noch nicht existiert
 
# product.clear() # löshct alle key Value Paare in einem Dictionary, das Dictionary selbst, bleibt aber bestehen.
# del product # löscht das komplette Dictionary
del product["preis"] # löscht den Key Value wert an der Stelle des angegebenen Keys
wert = product.pop("name") # löscht ebenfalls einen Key Value aus dem Dictionary und gibt den gelöschten Wert zurück
kopie_product = product.copy() # erstellt eine Kopie von einem Dictionary
 
print(wert)

# Eine Liste ist wie eine Einkaufsliste (Positionen zählen).
# Ein Dictionary ist wie ein Wörterbuch (du suchst nach einem Wort – dem Key – und bekommst die Bedeutung – den Value).