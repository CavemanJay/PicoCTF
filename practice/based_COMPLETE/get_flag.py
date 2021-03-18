#!/usr/bin/python3
from pwn import remote, context
import re


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


def get_encoded_from_prompt(prompt: str):
    target = re.findall('the .* as a word',
                        prompt)[0].replace('the ', "").replace("as a word", "").strip()

    return target


host, port = "jupiter.challenges.picoctf.org", 29956

context.log_level = 100

r = remote(host, port)
prompt = r.recvuntil('Input:').decode().splitlines()[2]

binary_word = get_encoded_from_prompt(prompt)
word = convert_binary_to_word(binary_word)
r.sendline(word)


prompt = r.recvuntil("Input:").decode().splitlines()[1]
octal_word = get_encoded_from_prompt(prompt)

r.sendline(convert_octal_to_word(octal_word))

prompt = r.recvuntil("Input:").decode().splitlines()[1]
hex_word = get_encoded_from_prompt(prompt)
r.sendline(convert_hex_to_word(hex_word))

print(re.findall('picoCTF{.*}', r.recvall().decode())[0])

r.close()
