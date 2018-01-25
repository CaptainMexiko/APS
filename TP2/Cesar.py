#!/usr/bin/python3


def CesarV2(inputText, mode, cle):
    res = ''
    if mode == 0:
        for c in inputText:
            tmp = ord(c) - cle
            if tmp < 0:
                tmp = tmp % 256
            res = res + chr(tmp)
        print(res)

    if mode == 1:
        for c in inputText:
            tmp = ord(c) + cle
            if tmp > 256:
                tmp = tmp % 256
            res = res + chr(tmp)
            pass
        print(res)


if __name__ == '__main__':
    inputText = open("Cesar.txt", "r")
    rT = inputText.read()
    decal = int(input("Veuillez entrer le décalage : "))
    print("Qu'elle mode voulez vous utiliser ?\n1 : chiffré\n0 : déchiffré")
    choix = int(input())
    CesarV2(rT, choix, decal)
