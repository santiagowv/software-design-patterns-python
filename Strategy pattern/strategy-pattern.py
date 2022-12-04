# it's a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.
# we create objects which represent various strategies and a context object whose behavior varies as per its strategy object. The strategy object changes the executing algorithm of the context object.
# the context isn't responsible for selecting and appropiate algorithm for the job. Instead, the client passes their desired strategy to the context.

from abc import ABC, abstractmethod

# pseudocode
class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: list):
        pass

class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: list) -> list:
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: list) -> list:
        return reversed(sorted(data))

class Context:
    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def do_some_business_logic(self, data: list) -> None:
        print("Context: Sorting data using the strategy configured")
        result = self.strategy.do_algorithm(data)
        result = [str(x) for x in result]
        print(", ".join(result))

if __name__ == "__main__":
    context = Context(ConcreteStrategyA())
    context.do_some_business_logic(data = [1, 2, 3, 8, 5])