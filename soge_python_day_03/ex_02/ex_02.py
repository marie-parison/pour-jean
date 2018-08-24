#!/usr/bin/python

class Titan(object):

    def __init__(self, name: str, age: int, size: float, speed: float):
        self._name = name
        self._age = age
        self._size = size
        self._speed = speed

test = Titan("Test", 26, 1.83, 2.0)

print(test.name)

