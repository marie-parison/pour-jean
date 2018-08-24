#!/usr/bin/python

import sys

def exercice():
    print len(sys.argv) - 1
    print >> sys.stderr, len(sys.argv)
 
if __name__ == '__main__':
    exercice()