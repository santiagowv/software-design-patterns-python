# it helps us separate components therefore it reduces coupling. This helps us write clean code.
# the basic idea of dependency inversion is to write our code in such a way that high level modules shouldn't depend on low level modules, both should depend on abstractions.

from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class AwsServer(Switchable):
    def turn_on(self):
        print("AwsSever: turned on...")

    def turn_off(self):
        print("AwsServer: turned off...")

class AzureServer(Switchable):
    def turn_on(self):
        print("AzureServer: turned on...")

    def turn_off(self):
        print("AzureServer: turned off...")

class ServerPowerSwitch:
    def __init__(self, s: Switchable):
        self.client = s
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True

az = AzureServer()
aw = AwsServer()
switch = ServerPowerSwitch(az)
switch.press()
switch.press()