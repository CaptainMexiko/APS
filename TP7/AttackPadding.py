#!/usr/bin/python3

import subprocess
import socket
import sys
import math


def makeSocket():
    s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 10345))
    return s


def oracle(modulo, cipher):
    s = makeSocket()
    k = int(math.ceil(math.log(modulo, 2)) / 8)
    print(k)
    s.sendall(cipher.to_bytes(k, "big"))
    data = s.recv(1024)
    print(data)
    return data.decode()[0] == "O"
    pass


if __name__ == '__main__':
    modulo = 10937931339312247509656572406274903349843133231885017160356929738133511786226962991787204115858820759611539959224249631809786361349407014616124627875981547
    exposant = 65537
    cipher = int( "2E82DBFA996C5475D820FE1CC2EEBFB0F430AE697B93BFDE802907FA422EFD308DFCEE7AFA8F4F280F1D6B88CAEBDAA3299CBBAE06D743D6603B417FF7F29839" , 16)
    print(oracle(modulo, cipher))
