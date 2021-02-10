import os
import re
import binascii

# https://stackoverflow.com/a/7397689

link = 'https://jupiter.challenges.picoctf.org/static/95be9526e162185c741259a75dffa0ab/whitepages.txt'

src = os.popen(
    F'curl -sL {link}').read().replace('\u2003', '0').replace(" ", '1')

n = int('0b'+src, 2)
string = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

flag = re.findall(r'picoCTF{.*}', string)[0]

print(flag)
