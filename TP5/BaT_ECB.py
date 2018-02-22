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


def makeList():
    dic = []
    for i in range(256):
        k = "a" * 15 + chr(i)
        c = ECB_oracle_chall12(k)[0:16]
        dic.append(c)
    return dic


def decode(listIn):
    listEnd = []
    tailleMax = len(ECB_oracle_chall12(""))
    k = 'a' * 15
    phrase = ECB_oracle_chall12(k)
    for index in range(tailleMax):
        for i in range(len(listIn)):
            print(index)
            print(i)
            if listIn[i] == phrase:
                listEnd.append(chr(i))
                pass
            pass
        pass
    return listEnd


if __name__ == '__main__':
    print(str(decode(makeList())))
    print("End")
