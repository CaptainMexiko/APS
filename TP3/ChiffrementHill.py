#!/usr/bin/python3

import random


def multiMatrice(matrice, vecteur, coeff):
    result = [[0] for _ in range(len(matrice))]
    for ligne in range(0, len(matrice)):
        newval = 0
        for elem in range(0, len(matrice)):
            newval += (matrice[ligne][elem] * vecteur[elem])
            pass
        result[ligne] = newval % coeff
        pass
    return result


def creaMatrice(valeur, taille):
    matrice = [[0] * taille for _ in range(taille)]
    for i in range(taille):
        for j in range(taille):
            matrice[i][j] = random.randint(0, valeur)
            pass
        pass
    return matrice


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)


def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n


def matriceIdent(taille):
    matrice = [[0] * taille for _ in range(taille)]
    for i in range(taille):
        matrice[i][i] = 1
    return matrice


def inverseMatrice(matrice, taille, coeff):
    ident = matriceIdent(taille)
    indexBonJ = 0
    indexBonI = 0
    ligne = 1
    trouve = False
    while ligne < taille:
        print(ligne)
        i = 0
        while not trouve and i < taille:
            for j in range(i, taille):
                if mulinv(matrice[j][i], coeff) is not None:
                    indexBonJ = j
                    indexBonI = i
                    trouve = True
                    break
                print(j)
                pass
            i += i
            pass
        ligne += ligne
        if not trouve:
            print("La matrice n'est pas inversible")
            return []
        if indexBonJ != ligne:
            matrice[ligne], matrice[indexBonJ], ident[ligne], ident[indexBonJ] = matrice[indexBonJ], matrice[ligne], ident[indexBonJ], ident[ligne]
        inv = mulinv(matrice[ligne][ligne], coeff)
        matrice[ligne] = [inv * x for x in matrice[ligne]]
        ident[ligne] = [inv * x for x in ident[ligne]]
    return ident


if __name__ == "__main__":
    valeur = 4
    taille = 3
    vecteur = [1, 3, 4, 5, 4, 6, 3, 6, 9, 2]
    matrice = creaMatrice(valeur, taille)
    print(matrice)
    ident = matriceIdent(taille)
    print(ident)
    res = inverseMatrice(matrice, taille, 26)
    print(res)
