#!/usr/bin/env python

f = open("./numbers.txt", "r")

for line in f:
    for word in line.split(','):
            print(word)