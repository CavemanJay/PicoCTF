from typing import Tuple
from icecream import ic
import re
ic.disable()

with open('VaultDoor8.java', 'r') as f:
    source = "".join(line
                     for line in f.readlines()
                     if not line.startswith("//"))


def switchBits(c: str, p1: int, p2: int):
    _c = ord(c)
    mask1 = 1 << p1
    mask2 = 1 << p2
    bit1 = _c & mask1
    bit2 = _c & mask2
    rest = _c & ~(mask1 | mask2)
    shift = p2-p1
    result = (bit1 << shift) | (bit2 >> shift) | rest

    ic(mask1, mask2, bit2, rest, shift, result, chr(result))
    return chr(result)


def unscramble(c: str, order: Tuple[int, int]):
    u = c
    for switch in order:
        u = switchBits(u, *switch)
    return u


tight_source = source.replace("\n", "")
uncommented_source = re.sub(r'/\*.*?\*/', "", tight_source)

bit_switches = re.findall(
    r'c\s+=\s+switchBits\(c,(\d+,\d+)\)', uncommented_source)
expected = re.findall(
    r'char\[\]\sexpected\s?=\s?{(.*?)}', uncommented_source)[0].strip().split(', ')
scrambled = (chr(int(hex_num, 16))
             for hex_num in expected)

switch_order = [tuple(map(int, switch.split(",")))
                for switch in bit_switches[::-1]]

flag = "".join(unscramble(c, switch_order) for c in scrambled)
flag = F"picoCTF{{{flag}}}"

print(flag)
