#!/usr/bin/python3


def CesarV2(inputText, mode, cle, outputText):
    res = ''
    if mode == 0:
        for c in inputText:
            tmp = ord(c) - cle
            if tmp < 0:
                tmp = tmp % 256
            res = res + chr(tmp)
        outputText.write(res)

    if mode == 1:
        for c in inputText:
            tmp = ord(c) + cle
            if tmp > 256:
                tmp = tmp % 256
            res = res + chr(tmp)
            pass
        outputText.write(res)


if __name__ == '__main__':
    inputText = open("CesarInput.txt", "r")
    outputText = open("CesarOutput.txt", "w")
    rT = inputText.read()
    decal = int(input("Veuillez entrer le décalage : "))
    print("Qu'elle mode voulez vous utiliser ?\n1 : chiffré\n0 : déchiffré")
    choix = int(input())
    CesarV2(rT, choix, decal, outputText)
    inputText.close()
    outputText.close()
