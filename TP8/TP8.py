#!/usr/bin/python3

import hashlib
from itertools import permutations

INPUT = "Lorem ipsum dolor sit amet, consectetur adipisicing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


def funch(textinput):
    hashsha256 = hashlib.sha256()
    hashsha256.update(textinput.encode())
    text_digest = hashsha256.hexdigest()
    res = text_digest[:4]
    return res


def hforint(intinput, textinput):
    returnedHash = 0;
    to_attempt = [''.join(p) for p in permutations(textinput)]
    to_attempt.remove(textinput)
    for attempt in to_attempt:
        returnedHash = funch(''.join(attempt))
        if returnedHash == intinput:
            return ''.join(attempt)
    return returnedHash

if __name__ == '__main__':
    funch("crypto")
    print(hforint("da2f", 'crypto'))
