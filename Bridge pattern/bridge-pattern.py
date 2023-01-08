# It's a structural design pattern that lets you split a large class or a set of closely related classes
# into two separate hierarchies (abstraction and implementation) which can be developed independently of each other

# Elements of bridge design pattern:
# - Abstraction: It is the core of the bridge design pattern and it provides the reference of the implementer.
# - Refined abstraction: It extends the abstraction to a new level where it takes the finer details one level above and hides the finer element from the implementers.
# - Implementer: It defines the interface for implementation classes. The interface does not need to correspond directly to the abstraction interface and can be very different.
# - Concrete implementer: Through the concrete implementation, it implements the above implementer.

from abc import ABC, abstractmethod

# pseudocode

class Abstraction(ABC):
    """
    The Abstraction defines the interface for the "control" part of the two class hierarchies.
    It mantains a reference to an object of the Implementation hierarchy and delegates all
    of the real work to this object
    """

    def __init__(self, implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with: {self.implementation.operation_implementation()}")

class ExtendedAbstraction(Abstraction):
    """
    You can extend the Abstraction without chaning the Implementation classes
    """

    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with: {self.implementation.operation_implementation()}")


class Implementation(ABC):
    """
    The Implementation defines the interface for all implementation classes. It
    doesn't have to match the Abstraction's interface. In fact, the two
    interfaces can be entirely different. Typically the Implementation interface
    provides only primitive operations, while the Abstraction defines higher-
    level operations based on those primitives.
    """

    @abstractmethod
    def operation_implementation(self) -> str:
        pass    

class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."

class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


def client_code(abstraction: Abstraction) -> None:
    """
    Except for the initialization phase, where an Abstraction object gets linked
    with a specific Implementation object, the client code should only depend on
    the Abstraction class. This way the client code can support any abstraction-
    implementation combination.
    """
    
    print(abstraction.operation())


if __name__ == "__main__":
    """
    The client code should be able to work with any pre-configured abstraction-
    implementation combination.
    """

    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)