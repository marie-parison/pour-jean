#!/usr/bin/python

def convert_me_to_a_dict(list):
    return { key : (type(item).__name__, item) for key,item in enumerate(list)}

print(convert_me_to_a_dict(["test", 12, 12.68]))
