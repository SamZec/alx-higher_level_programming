#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    first = None
    if lenght != 0:
        first = sentence[0]
    return lenght, first
