#!/usr/bin/python3

import base64


def distanceHamming(str1, str2):
    diffsBit = 0
    for char1, char2 in zip(str1, str2):
        diffsBit += bin_weight(ord(char1) ^ ord(char2))
    pass
    return diffsBit


def bin_weight(x):
    return bin(x).count('1')


def decode(ligne2dec):
    stuffDec = base64.b64decode(ligne2dec)
    return stuffDec


def getKeySize(fileIn):
    test = fileIn.readline()
    print(decode(test))


fileDec = open("message1.txt", 'r')
getKeySize(fileDec)
