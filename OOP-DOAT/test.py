### Konzeption der Fabrik-Methode
from abc import ABC, abstractmethod


# 1. Product
class Product(ABC):
    """
    Definiert das gemeinsame Interface für alle Objekte, die vom Creator erzeugt werden können.
    """
    @abstractmethod
    def operation(self) -> str:
        pass

# 2. Konkreten Produkten als konkrete Implementierungen des Product-Interfaces

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "Operation of ConcreteProduct1"

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "Operation of ConcreteProduct2"


# 3. Creator
class Creator(ABC):
    """
    Deklariert die Factory Method, die ein Objekt vom Typ Product zurückgibt.
    Enthält meist Geschäftslogik, die mit Produkten arbeitet, ohne deren konkrete Klassen zu kennen.
    """

    @abstractmethod
    def factory_method(self):
        """
        Standardimplementierung der Fabrikmethode
        """
        pass

    def some_operation(self) -> str:
        """
        Kern der Geschäftslogik, welche in jeder Fabrik enthalten sein muss.
        """

        # Fabrikmethode (der Unterklasse), um ein konkretes Produkt zu erzeugen
        product = self.factory_method()

        # Hier kann die (allgemeine Geschäftslogik) auf das Produkt angewendet werden
        result = f'Creator: Creator\'s Code has just worked with {product}'

        return result


# 4. Concrete Creator: Überschreiben der Factory Method, um konkrete Produkte zu erzeugen.

class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


# Client Code
def client_code(creator: Creator):
    """
    Der Client Code arbeitet mit einer Instanz einer konkreten Fabrik.
    In der Signatur wird jedoch nur die Fabrikklasse genutzt.
    """
    print(f"Client: Is not aware of the creator's class, but it still works!\n"
          f"{creator.some_operation()}", end="\n")


# Code aufrufen
print("App: Launched with ConcreteCreator1")
client_code(ConcreteCreator1())

print("App: Launched with ConcreteCreator2")
client_code(ConcreteCreator2())