#!/usr/bin/python3

def multiple_returns(sentence):
    if not len(sentence):
        sentence[0] = None
    i = len(sentence)
    j = sentence[0]
    return(i, j)
