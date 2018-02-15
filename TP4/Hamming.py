#!/usr/bin/python3

import base64


def distanceHamming(str1, str2):
    diffsBit = 0
    for char1, char2 in zip(str1, str2):
        diffsBit += bin_weight(ord(chr(char1)) ^ ord(chr(char2)))
    pass
    return diffsBit


def bin_weight(x):
    return bin(x).count('1')


def getKeySize(name):
    listKey = []
    for keysize in range(2, 42):
        fileIn = open(name, "r")
        for ligne in range(1, 6):
            print("KeySize = ", keysize)
            listDist = []
            linetest = base64.b64decode(fileIn.readline())
            newline = linetest[keysize:]
            print("Ligne decal = ", newline)
            test = distanceHamming(newline, linetest[:-keysize])
            print("Val distance = ", test)
            listDist.append(test)
            print("List Distance ", listDist)
            ligne += 1
        listKey.append(listDist)
    print(listKey)


getKeySize("message1.txt")
