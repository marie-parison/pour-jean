#!/usr/bin/python

from ex_03 import Titan
from datetime import date

class DeviantTitan(Titan):

    def __init__(self, name: str, age: int, size: float, speed: float, deviance_index: int, errors: int):
        
        super().__init__(name: str, age: int, size: float, speed: float)
        
        if 1 <= deviance_index <= 10:
            self.__deviance_index = deviance_index
        else:
            raise ValueError()
        self.__errors = errors

    def getDeviance_index(self):
        return self.__deviance_index
    
    def setDeviance_index(self, deviance_index: int):
        self.__deviance_index = deviance_index
    
    def getErrors(self):
        return self.__errors
    
    def setErrors(self, errors: int):
        self.__errors = errors


class RoyalTitan(Titan):

    def __init__(self, name: str, age: int, size: float, speed: float, family_name: str, transformation_date: date):

        super().__init__(name: str, age: int, size: float, speed: float)

        self.__family_name = family_name
        self.__transformation_date = transformation_date
    
    def getFamily_name(self):
        return self.__family_name

    def setFamily_name(self, family_name: str):
        self.__family_name = family_name

    def getTransformation_date(self):
        return self.__transformation_date

    def setTransformation_date(self, transformation_date: date):
        self.__transformation_date = transformation_date


deviant = DeviantTitan(11, 4)
print(deviant.getDeviance_index())