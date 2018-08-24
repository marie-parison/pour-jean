#!/usr/bin/python

def test():
    for number in [str(item) for item in range(0, 10)]:
        yield number

def print_me_separated(generator):
    separator = "|"
    print (separator.join(generator))

print_me_separated(test())