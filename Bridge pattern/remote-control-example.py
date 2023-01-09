from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint

class Device(ABC): # implementer
    def __init__(self):
        self.is_enabled = False
        self.volume = randint(1, 100) / 100
        self.channel = randint(1, 20)
    
    @abstractmethod
    def is_enabled(self) -> None:
        pass

    @abstractmethod
    def enable(self) -> None:
        pass

    @abstractmethod
    def disable(self) -> None:
        pass

    @abstractmethod
    def get_volume(self) -> None:
        pass

    @abstractmethod
    def set_volume(self, percent:int) -> None:
        pass

    @abstractmethod
    def get_channel(self) -> None:
        pass

    @abstractmethod
    def set_channel(self, channel:int) -> None:
        pass

class TVDevice(Device): # concrete implementer
    def is_enabled(self) -> None:
        if self.is_enabled:
            return True
        else:
            return False

    def enable(self) -> None:
        if self.is_enabled:
            print("The TV is already on")
        else:
            self.is_enabled = True
            print("The TV was turned on")

    def disable(self) -> None:
        if self.is_enabled:
            self.is_enabled = False
            print("The TV was turned off")
        else:
            print("The TV is already off")

    def get_volume(self) -> None:
        print(f"The volume of your TV is: {self.volume}")

    def set_volume(self, percent:int) -> None:
        percent = percent / 100
        self.volume += percent
        if self.volume < 0:
            self.volume = 0
        print(f"Your TV was set to volume: {self.volume}")

    def get_channel(self) -> None:
        print(f"Your TV is in channel: {self.channel}")

    def set_channel(self, channel:int = 1) -> None:
        if channel == 1:
            self.channel += 1
        else:
            self.channel = channel
        if self.channel < 1:
            self.channel = 1
        print(f"Your TV was set to channel: {self.channel}")

class RadioDevice(Device): # concrete implementer
    def is_enabled(self) -> None:
        if self.is_enabled:
            return True
        else:
            return False

    def enable(self) -> None:
        if self.is_enabled:
            print("The radio is already on")
        else:
            self.is_enabled = True
            print("The radio was turned on")
    
    def disable(self) -> None:
        if self.is_enabled:
            self.is_enabled = False
            print("The radio was turned off")
        else:
            print("The radio is already off")

    def get_volume(self) -> None:
        print(f"The volume of your radio is: {self.volume}")

    def set_volume(self, percent:int) -> None:
        percent = percent / 100
        self.volume += percent
        if self.volume < 0:
            self.volume = 0 
        print(f"Your radio was set to volume: {self.volume}")

    def get_channel(self) -> None:
        print(f"Your radio is in channel: {self.channel}")
    
    def set_channel(self, channel:int = 1) -> None:
        if channel == 1:
            self.channel += 1
        else:
            self.channel = channel
        if self.channel < 1:
            self.channel = 1
        print(f"Your radio was set to channel: {self.channel}")

class Remote(ABC): # abstraction
    def __init__(self, device:Device):
        self.device = device

    def toogle_power(self) -> None:
        if self.device.is_enabled():
            self.device.enable()
        else:
            self.device.disable()

    def volume_up(self) -> None:
        percent = 1
        self.device.set_volume(percent)

    def volume_down(self) -> None:
        percent = -1
        self.device.set_volume(percent)
    
    def channel_up(self) -> None:
        self.device.set_channel()

    def channel_down(self) -> None:
        self.device.set_channel()
        
class AdvancedRemote(Remote): # refined abstraction
    def mute(self) -> None:
        self.device.set_volume(- 100)

class PremiumRemote(Remote): # refined abstraction
    def set_premium_channel(self):
        print("Premium channels are all channels over 100")
        channel = int(input("Please input a premium channel:"))
        self.device.set_channel(channel)

if __name__ == "__main__":
    standard_remote = Remote(TVDevice())
    standard_remote.volume_up()
    standard_remote.volume_down()
    standard_remote.channel_down()
    standard_remote.channel_up()

    advanced_remote = AdvancedRemote(RadioDevice())
    advanced_remote.mute()

    premium_remote = PremiumRemote(TVDevice())
    premium_remote.volume_up()
    premium_remote.set_premium_channel()