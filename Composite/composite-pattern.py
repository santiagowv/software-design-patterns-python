# Composite is a structural design pattern that lets you compose objects into tree structures and then work with these structures as if they were individual objects.

# 1. The Component interface describes operations that are common to both simple and complex elements of the three.
# 2. The Leaf is a basic element of a tree that doesn’t have sub-elements. Usually, leaf components end up doing most of the real work, since they don’t have anyone to delegate the work to.
# 3. The Container (aka composite) is an element that has sub-elements: leaves or other containers. A container doesn’t know the concrete classes of its children. It works with all sub-elements ony via the component interface.
#    Upon receiving a request, a container delegates the work to its sub-elements, processes intermediate results and then returns the final result to the client.
# 4. The Client works with all elements through the component interface. As a result, the client can work in the same way with both simple or complex elements of the three.

from __future__ import annotations
from abc import ABC, abstractmethod

class Component(ABC):
    """
    The base Component class declares common operations for both simple and
    complex objects of a composition.
    """
    def __init__(self, id:tuple(str)) -> None:
        self.id = id
        self._children = []

    @abstractmethod
    def operation(self) -> str:
        pass

class Leaf(Component):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.

    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-components.
    """
    def operation(self) -> None:
        print("\t", end ="")
        print(self.id)

class Composite(Component):
    """
    The Composite class represents the complex components that may have
    children. Usually, the Composite objects delegate the actual work to their
    children and then "sum-up" the result.
    """
    def add(self, component: Component) -> None:
        self._children.append(component)
    
    def remove(self, component: Component) -> None:
        self._children.remove(component)
    
    def operation(self) -> None:
        print(self.id)
        for child in self._children:
            print("\t", end ="")
            child.operation()

if __name__ == "__main__":
    top_level_menu = Composite(("User", "1"))
    sub_level2 = Composite(("User", "2"))
    sub_level3 = Composite(("User", "3"))
    sub_level_item21 = Leaf(("Item", "2.1"))
    sub_level_item22 = Leaf(("Item", "2.2"))
    sub_level_item31 = Leaf(("Item", "3.1"))
    sub_level_item32 = Leaf(("Item", "3.2"))

    sub_level2.add(sub_level_item21)
    sub_level2.add(sub_level_item22)
    
    sub_level3.add(sub_level_item31)
    sub_level3.add(sub_level_item32)

    top_level_menu.add(sub_level2)
    top_level_menu.add(sub_level3)

    top_level_menu.operation()