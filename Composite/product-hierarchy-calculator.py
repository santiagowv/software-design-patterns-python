from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def operation(self) -> int:
        pass

class Product(Item):
    def __init__(self, name:str, price:int) -> None:
        self.name = name
        self.price = price

    def operation(self) -> int:
        return self.price

class Box(Item):
    def __init__(self) -> None:
        self._children = []

    def add(self, item: Item) -> None:
        self._children.append(item)

    def remove(self, item: Item) -> None:
        self._children.remove(item)
    
    def operation(self) -> int:
        total = 0
        for child in self._children:
            price = child.operation()
            total += price
        return total

if __name__ == "__main__":
    item1 = Product("coat", 22)
    item2 = Product("shoe", 100)
    item3 = Product("Jacket", 44)
    item4 = Product("Socks", 5)

    box = Box()
    box.add(item1)
    box.add(item2)

    box1 = Box()
    box1.add(item3)
    box1.add(item4)

    box.add(box1)

    print(box.operation())
