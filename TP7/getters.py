#!/usr/bin/python2.7

from TP7_helpers import *
import subprocess


def getKeyPub():
    raw_key = subprocess.check_output(['./TP7_oracle', 'pubkey'])
    modulo, e = extract_pubkey(raw_key)
    return modulo, e

def getCipher():
    cipher = subprocess.check_output(['./TP7_oracle', 'flag'])
    return cipher

if __name__ == '__main__':
    modulo, e = getKeyPub()
    print(modulo)
    print("\n")
    print(e)
    print("\n")
    cipher = getCipher()
    print(cipher)
