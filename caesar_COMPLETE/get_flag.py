#!/usr/bin/python3
import os
ciphertext = os.popen(
    "curl -s https://2019shell1.picoctf.com/static/16895b37d67ca673cc69c4d096444bfb/ciphertext").read()


def get_possible_shifts(ciphertext):
    possibilities = []
    for i in range(1, 26):
        possibilities.append(shift_characters(ciphertext, i))
    return possibilities


def shift_characters(text: str, shift: int):
    current = ""
    for c in text:
        shifted = ord(c)+shift
        while shifted > 122:
            shifted -= 26
        current += chr(shifted)
    return current


ciphertext = ciphertext.split("{")[1].replace("}", "")
# possibilities = get_possible_shifts(ciphertext)
flag = F"picoCTF{{{shift_characters(ciphertext, 14)}}}"
print(flag)
