#!/usr/bin/python

class Titan(object):

    def __init__(self, name: str, age: int, size: float, speed: float):
        self._name = name
        self._age = age
        self._size = size
        self._speed = speed

    def getName(self):
        return self._name

    def setName(self, name: str):
        self._name = name

    def getAge(self):
        return self._age
    
    def setAge(self, age: int):
        self._age = age

    def getSize(self):
        return self._size
    
    def setSize(self, size: float):
        self._size = size

    def getSpeed(self):
        return self._speed
    
    def setSpeed(self, speed: float):
        self._speed = speed
    
    def destroy(self):
        print("Deeesssttrroyyy !")

test = Titan("Test", 26, 1.83, 2.0)
print(test.getName())
test.setName("NewName")
print(test.getName())
test.destroy()
