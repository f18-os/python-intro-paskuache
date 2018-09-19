#!/usr/bin/env python3
import os

def count(a, b):
    inp = open('./'+a, r)
    out = open('./'+b, r+)
    for word in inp.read().split():
        if word not in pal:
            out.append(word, ' 1')
        else:
            out[1] += 1
                
