#!/usr/bin/env python3

def print_fibonacci(length):
    new_sequence = []
    if length > 0:
        new_sequence.append(0)
    if length > 1 :
        new_sequence.append(1)
    if length > 2:
        i=0
        while i <= (length - 3):
            new_value = new_sequence[i] + new_sequence[i+1]
            new_sequence.append(new_value)
            i+=1
    print(new_sequence)
