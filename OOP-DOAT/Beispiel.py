# Einfaches Prototype-Beispiel

class Prototype:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def clone(self):
        # Erstelle einfach ein neues Objekt mit den gleichen Werten
        return Prototype(self.name, self.number)


# Wir erstellen ein Objekt
original = Prototype("MeinObjekt", 42)

# Wir klonen es
kopie = original.clone()

# Inhalte zeigen
print("Original:", original.name, original.number)
print("Kopie:   ", kopie.name, kopie.number)

# Prüfen, ob es dasselbe Objekt ist
print("Gleiches Objekt?", original == kopie)  # False
print("Gleicher Typ?", type(original) == type(kopie))  # True