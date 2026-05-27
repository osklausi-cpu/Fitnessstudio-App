"""
    Die Multiplikation der ganzen Zahlen kann x und y kann auch als x maliges addieren der Zahl y gelöst werden
    Erstellen Sie eine rekursive Funktion für diese Operation
 """
 
# 4 * 3 = 12
# 12 = 3 + 3 + 3 + 3
 
 
def rekursive_funktion(x, y):
    if x == 0:
        return 0
    else:
       print(f"Hier ist die Zahl x: {x}, Und hier ist y: {y}")
       return y + rekursive_funktion(x-1, y) # bei jeden Aufruf der Funktion selbst, wird x um ein veringert
 
print(rekursive_funktion(3, 4))
 
 
 
"""
    Eine rekursive Funktion ist eine Funktion die sich selbst aufruft.
"""