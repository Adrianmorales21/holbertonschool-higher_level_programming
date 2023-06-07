#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        sentence[0] = None
        return None
    first_char = sentence[0]
    return len(sentence), first_char
