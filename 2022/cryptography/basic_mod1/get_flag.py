#!/usr/bin/env python3

# Read message in as list of numbers
with open('message.txt', 'r') as f:
    message = (int(num) for num in f.readline().split(" ") if num != '')


def decode(num: int):
    modded = num % 37
    if modded == 36:
        return "_"
    elif modded in range(26, 35+1): # Handle decimal digits
        return str(modded-26)
    elif modded in range(0, 25+1): # Handle alphabet characters 
        return chr(modded+65)
    else:
        return None


decoded_message = ''.join(map(decode, message))
flag = F"picoCTF{{{decoded_message}}}"

print(flag)
