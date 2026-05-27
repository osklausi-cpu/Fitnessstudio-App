#Möglicher Umgang mit Zeit: 
 
import time
 
print(time.localtime())
print(f"{time.localtime()[2]}.{time.localtime()[1]}.{time.localtime()[0]}") # Gibt uns das Lokale Zeitkonstrukt als struct time Object zurück
 
 
print(time.time()) # Liefert uns die Zeit in Sekunden seit 1970 zurück
 
 
print(time.strftime('%H:%M:%S')) # liefert die aktuelle Uhrzeit zurück