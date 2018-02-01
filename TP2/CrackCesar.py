#!/usr/bin/python3

from collections import OrderedDict
from operator import itemgetter


def crackCesar(inp):
    dicoFreq = {}
    for c in inp:
        if c not in dicoFreq:
            dicoFreq[c] = inp.count(c) / len(inp)
        pass
    dicoEnd = OrderedDict(sorted(dicoFreq.items(), key=itemgetter(1)))
    possible = sorted(dicoEnd.keys())[-2]
    print(possible)
    print(ord(possible))
    print(ord('e'))
    cle = ord(possible) - ord('e')
    print(cle)
    res = ''
    for c in inp:
        tmp = ord(c) - cle
        if tmp < 0:
            tmp = tmp % 256
        res = res + chr(tmp)
    print(res)


if __name__ == '__main__':
    chif = open('CesarOutput.txt', 'r')
    red = chif.read()
    crackCesar(red)
