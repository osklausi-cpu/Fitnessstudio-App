### Konzeption eines Prototyps

from abc import ABC, abstractmethod
import copy

# 1. Prototype-Interface
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


# 2. Concrete Prototype
class ConcretePrototype(Prototype):
    def __init__(self, some_number: int, some_string: str, some_list: list):
        self.__some_number = some_number
        self.__some_string = some_string
        self.__some_list = some_list

    def clone(self):
        some_number = copy.deepcopy(self.__some_number)
        some_string = copy.deepcopy(self.__some_string)
        some_list = copy.deepcopy(self.__some_list)

        return ConcretePrototype(some_number, some_string, some_list)

# Optional: Subclass
class SubclassPrototype(ConcretePrototype):
    def __init__(self, some_number: int, some_string: str, some_list: list, extra):
        super().__init__(some_number, some_string, some_list)
        self.__extra = extra

    def clone(self):
        return SubclassPrototype(
            copy.deepcopy(self.__some_number),
            copy.deepcopy(self.__some_string),
            copy.deepcopy(self.__some_list),
            copy.deepcopy(self.__extra)
        )

# 3. Client
def client_code(prototype: Prototype):
    clone_of_object = prototype.clone()
    print("Content:")
    print(clone_of_object.__dict__)
    print("\n")
    print("Is it the same object as the prototype?", prototype == clone_of_object)
    print("Is it the same type as the prototype?", isinstance(prototype, type(clone_of_object)))


prototype = ConcretePrototype(18, "abcd", [0,1, {"key": "value"}, [1,2,3], (8,9)])
client_code(prototype)
