#!/usr/bin/python3
import os
ciphertext = open("ciphertext").read()


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
possibilities = get_possible_shifts(ciphertext)

flag = F"picoCTF{{{possibilities[-4]}}}"
print(flag)
