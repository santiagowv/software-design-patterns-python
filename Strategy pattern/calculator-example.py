from abc import ABC, abstractmethod
from functools import reduce

class MathOperation(ABC):
    @abstractmethod
    def operation(self, data: list[int]) -> float:
        pass

class Multiplication(MathOperation):
    def operation(self, data: list[int]) -> float:
        result = reduce(lambda x,y:x*y, data)
        return result

class Addition(MathOperation):
    def operation(self, data: list[int]) -> float:
        result = sum(data)
        return result

class Substraction(MathOperation):
    def operation(self, data: list[int]) -> float:
        new_list = sorted(data, reverse = True)
        result = reduce(lambda x,y:x-y, new_list)
        return result

class Calculator:
    def __init__(self, measure: MathOperation) -> None:
        self.measure = measure
        self.sets = []

    def create_operation(self, values: list[int]) -> None:
        self.sets.append(values)

    def result(self, result):
        print("The data...")
        print("Is being processed...")
        print(f"The result is {result}")

    def do_operations(self):
        for o in self.sets:
            self.result(result = self.measure.operation(o))


if __name__ == "__main__":
    app = Calculator(Multiplication())
    app.create_operation([2, 3, 4])
    app.create_operation([2, 2])
    app.create_operation([3, 4])
    app.do_operations()