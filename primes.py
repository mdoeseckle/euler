#!/usr/bin/python

from math import sqrt

def is_prime(value):
    maxCandidate = int(sqrt(value))

    if(value % 2 == 0):
        return False

    for candidate in range(3, maxCandidate + 1, 2):
        if(value % candidate == 0):
            return False

    return True
