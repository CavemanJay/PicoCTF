import re
from pwn import p32

with open("VaultDoor7.java", 'r') as f:
    source = f.read()


def chars(val):
    return p32(val, endian="big").decode()


flag_ints = map(int, re.findall(r'== (\d+)', source))
flag = "".join(map(chars, flag_ints))

print(F"picoCTF{{{flag}}}")
