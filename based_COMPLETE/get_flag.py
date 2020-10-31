#!/usr/bin/python3
# command = nc 2019shell1.picoctf.com 28758


def convert_binary_to_word(binary: str):
    binary = binary.split()
    result = ""
    for num in binary:
        result += chr(int(num, 2))
    return result


def convert_octal_to_word(decimal: str):
    decimal = decimal.split(" ")
    result = ""
    for num in decimal:
        result += chr(int(num, 8))
    return result


def convert_hex_to_word(hex: str):
    return bytes.fromhex(hex).decode('utf-8')


binary = "01100110 01100001 01101100 01100011 01101111 01101110"
print(convert_binary_to_word(binary))

octal = "164 141 142 154 145"
print(convert_octal_to_word(octal))

hex = "6c616d70"
print(convert_hex_to_word(hex))