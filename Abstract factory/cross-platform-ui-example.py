# The Abstract Factory interface declares a set of creation methods that the client 
# code can use to produce different types of UI elements. Concrete factories correspond 
# to specific operating systems and create the UI elements that match that particular OS.

from __future__ import annotations
from abc import ABC, abstractmethod

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        print("A button was added to the windows UI.")
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        print("A checkbox was added to the windows UI.")
        return WinCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        print("A button was added to the mac UI.")
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        print("A checkbox was added to the mac Ui.")
        return MacCheckbox()

class Button(ABC):
    def __init__(self):
        self.is_active = False    
    
    @abstractmethod
    def press(self) -> None:
        pass

class Checkbox:
    def __init__(self):
        self.is_active = False
    
    @abstractmethod
    def press(self) -> None:
        pass

class WinButton(Button):
    def press(self) -> None:
        if self.is_active:
            print("Your windows button was deactivated.")
            self.is_active = False
        else:
            print("Your windows button was activated.")
            self.is_active = True

class MacButton(Button):
    def press(self) -> None:
        if self.is_active:
            print("Your mac button was deactivated.")
            self.is_active = False
        else:
            print("Your mac button was activated.")
            self.is_active = True

class WinCheckbox(Checkbox):
    def press(self) -> None:
        if self.is_active:
            print("Your windows checkbox was deactivated.")
            self.is_active = False
        else:
            print("Your windows checkbox was activated.")
            self.is_active = True

class MacCheckbox(Checkbox):
    def press(self) -> None:
        if self.is_active:
            print("Your mac checkbox was deactivated.")
            self.is_active = False
        else:
            print("Your mac checkbox was activated.")
            self.is_active = True

class Application:
    def __init__(self, factory:GUIFactory):
        self.factory = factory

    def create_ui(self):
        print("Initializing interface...")
        button = self.factory.create_button()
        checkbox = self.factory.create_checkbox()
        print("UI interface finished.")
        return [button, checkbox]

def main() -> None:
    op_system = int(input("Select an operating system (windows:1/mac:2):"))
    if op_system == 1:
        factory = WinFactory()
    elif op_system == 2:
        factory = MacFactory()
    app = Application(factory)
    ui_objects = app.create_ui()
    for e in ui_objects:
        e.press()

if __name__ == "__main__":
    main()