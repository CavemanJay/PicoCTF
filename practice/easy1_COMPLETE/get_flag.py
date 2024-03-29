#!/usr/bin/python3
# Taken from: https://gist.github.com/dssstr/aedbb5e9f2185f366c6d6b50fad3e4a4#file-vigenere-py


def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext


ciphertext = "UFJKXQZQUNB"
key = "SOLVECRYPTO"
flag = F"picoCTF{{{decrypt(ciphertext, key)}}}"
print(flag)
