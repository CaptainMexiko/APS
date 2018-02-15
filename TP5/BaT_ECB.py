#!/usr/bin/python

from tools import *


def blockSize(textIn):
    taille = 0
    taillePrec = 0
    for i in range(128):
        c = ECB_oracle_chall12("a" * i)
        taillePrec = taille
        taille = len(c)
        if taille != taillePrec and taillePrec != 0:
            return taille - taillePrec
            pass
        pass


def makeDico():
    dic = {}
    for i in range(256):
        k = "a" * 15 + chr(i)
        c = ECB_oracle_chall12(k)
        dic[chr(i)] = c
    return dic


def decode(dico):
    k = 'a' * 15
    phrase = ECB_oracle_chall12(k)
    for i, val in dico.items():
        print("keys = " + i)
        if val == phrase:
            return i[15]
            pass
        pass
    return"-1"


if __name__ == '__main__':
    print(str(decode(makeDico())))
