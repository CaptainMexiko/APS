#!/usr/bin/python2.7

from Crypto.PublicKey import RSA
from base64 import b64decode


def divceil(a, b):
    # Return ceil(a/b)
    c = a // b
    if(b * c != a):
        return c + 1
    return c


def euclide_etendu(a, b):
    # Return (g,u,v) such that g = a.u + b.v
    u = 1
    v = 0
    s = 0
    t = 1
    while(b > 0):
        q = a // b
        r = a % b
        a = b
        b = r
        tmp = s
        s = u - q * s
        u = tmp
        tmp = t
        t = v - q * t
        v = tmp
    return (a, u, v)  # (pgcd,u,v)


def modinv(a, n):
    # Return the inverse of a mod n
    t = euclide_etendu(a, n)  # t = (pgcd,u,v)
    if(t[0] == 1):
        return t[1] % n
    else:
        raise ValueError("Input not inversible")


def extract_pubkey(pem_key):
    # Input : string containing the base64 encoded RSA public key
    # Return (N,e) where N is the modulo and e the exponent.
    pem_key = pem_key.lstrip("-----BEGIN PUBLIC KEY-----\n")
    pem_key = pem_key.rstrip("-----END PUBLIC KEY-----")
    pem_key = pem_key.replace("\n", "")
    key = b64decode(pem_key)
    pubkey = RSA.importKey(key)
    return (pubkey.n, pubkey.e)
