class SingletonMeta(type):

    _instances = {} # statische Variable
    def __call__(cls, *args, **kwargs):
        """
        Aufruf der Klasse im Code greift auf diesen Code zu.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        print("Doing business!")


def client_code():

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works!")
    else:
        print("Singleton failed!")

client_code()
