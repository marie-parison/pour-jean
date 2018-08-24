#!/usr/bin/python

def format_my_args(*args):

    expressions = {int : lambda x : "i^:" + str(x), float : lambda x : "ff::" + str(x), str : lambda x : "[[" + x + "]]"}

    for arg in args:
        if type(arg) in expressions:
            print(expressions[type(arg)](arg))
        else :
            print("Unknown value")

format_my_args(12, "test", 18.1, [])