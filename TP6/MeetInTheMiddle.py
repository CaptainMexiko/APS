#!/usr/bin/python3
import subprocess
import base64

def createKey(list_key):
    taille_key = 8
    listKey = []
    for index in range(1, taille_key + 1):
        newKey = [[index] * taille_key]
        for key in range(1, len(list_key)):
            for offset in range(1, taille_key):
                keyOff = newKey[0]
                keyOff[offset] = key
                listKey.append(keyOff)
        listKey.append(newKey)
    return listKey


def MiM(listKey):
    plainText = base64.b64encode(b'Message sur 16o.')
    listCipher = {}
    for index in range(len(listKey)):
        keyTab = listKey[index]
        key = ""
        for i in range(len(keyTab)):
            key = key + str(keyTab[i])
        listCipher[key] = subprocess.check_output(["./weakCipher_enc", plainText, key])
    for index in range(len(listKey)):
        keyTab = listKey[index]
        key = ""
        for i in range(len(keyTab)):
            key = key + str(keyTab[i])
        deCipher = subprocess.check_output(["./weakCipher_dec", cipher, key])
        if deCipher in listCipher.values():
            # on retourne la clé correspondant à la valeur de listCipher correspondant à deCipher
    # pour chaque dechiffrage que l'on fait, on compare le résultat avec les valeurs dans listCipher, cela permet de retrouver les clé utilisé pour chiffré le message quand l'on tombe sur deux valeurs identiques
# Pour la question 2 on utilise l'oracle de déchiffrement deux fois, une première fois avec la première clé, la deuxième fois on utilise le résultat de la première fois que l'on déchiffre avec la deuxième clé
list_key = [1, 2, 3, 7]
# impossible de créer toutes les clés, je continue le tp comme si c'était bon
MiM(createKey(list_key))
