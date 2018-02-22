import subprocess
import base64

# -*- coding: utf-8 -*-
# TP noté APS -- 22/02/2018 -- 2h

# Message chiffré par 'blackbox' intercepté -- Objectif: le déchiffrer.
intercepted_cipher = b'LS1IZWxsbyBXb3JsZCEtLQ=='

# Le système de chiffrement 'blackbox' consiste en 'weakCipher' appliqué
# deux fois avec des clés différentes.
# On sait par ailleurs que les deux clés sont numériques et ne contiennent
# pas les chiffres 59468.

# Question 1: Retrouver les clés en faisant un Meet-in-the-Middle

# Le système de chiffrement est linéaire.
# En connaissant le chiffrement de 129 messages bien choisis,
# il est possible de déchiffrer le message.

# Question 2: Déchiffrer le message intercepté avec cette méthode.
# *points bonus* Résoudre cette question sans utiliser l'oracle de déchiffrement.


# Exemple de code d'interface pour utiliser les binaires ###

# note: les programmes prennent en entrée des données encodées en base64

plain = base64.b64encode(b'Message sur 16o.')
print("clair:", plain)

key = base64.b64encode(b'01234567')
# note: attention au type bytes.
# pour une variable entière i, on peut utiliser utiliser str.encode(str(i))
print("clé:", key)

cipher = subprocess.check_output(["./weakCipher_enc", plain, key])
print("chiffré:", cipher)

cipher_dec = subprocess.check_output(["./weakCipher_dec", cipher, key])
print("déchiffré:", cipher_dec)
print("déchiffré et décodé:", base64.b64decode(cipher_dec))
