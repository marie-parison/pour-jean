#!/usr/bin/python

def repeat_me(number):
    def decorator(function):
        def wrapper():
            for i in range(number):
                function()
        return wrapper
    return decorator

@repeat_me(2)
def test():
    print("Hello")

test()