#!/usr/bin/python

def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence[0] = None
    i = len(sentence)
    j = sentence[0]
    return(i, j)
