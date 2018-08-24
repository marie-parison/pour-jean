#!/usr/bin/python

def create_me_a_dico(list):
    return { tupple[0] : tupple [1] for tupple in list}

print(create_me_a_dico([(0, 'test'), ("12", "test2"), (2, 12)]))