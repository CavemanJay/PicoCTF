#!/usr/bin/env python3

# Read message in as list of numbers
with open('message.txt', 'r') as f:
    message = (int(num) for num in f.readline().split(" ") if num != '')

MODULUS = 41

# Mod all numbers by 41
message = (num % MODULUS for num in message)
# Find the modular inverse for each num
message = (pow(num, -1, MODULUS) for num in message)


def decode(num: int):
    if num in range(1, 26+1):
        return chr(num+64)
    elif num in range(27, 36+1):
        return str(num - 27)
    elif num == 37:
        return "_"
    else:
        return None

decoded_message = ''.join(map(decode, message))
flag = F"picoCTF{{{decoded_message}}}"
print(flag)
