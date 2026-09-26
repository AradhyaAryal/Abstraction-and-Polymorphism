from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self): pass

class TV(Device):
    def turn_on(self): print("TV on")

class Light(Device):
    def turn_on(self): print("Light on")

TV().turn_on()
Light().turn_on()