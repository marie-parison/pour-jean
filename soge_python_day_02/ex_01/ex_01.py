#!/usr/bin/python

def get_my_generator(*args):
    for arg in args:
        yield arg

generator = get_my_generator(1, 2)

for i in generator:
    print(i)