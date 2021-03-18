#!/usr/bin/python3
import os
from collections import namedtuple
from operator import attrgetter
src = open("VaultDoor1.java").read()
src = src[src.find("checkPassword(String pass"):].split("\n")
src.pop(0)
src.pop(33)
src.pop(34)
src.pop(33)
src.pop(0)

for x, line in enumerate(src):
    src[x] = line.lstrip()


def get_index(line: str):
    start = line.find("(")+1
    index = line[start:start+2]
    if ")" in index:
        index = line[start:start+1]
    return int(index)


def get_part(line: str):
    return line.split("'")[1]


FlagPart = namedtuple('FlagPart', ['index', 'part'])
dictionary = []
for line in src:
    index = get_index(line)
    part = get_part(line)
    dictionary.append(FlagPart(index, part))

dictionary = sorted(dictionary, key=attrgetter('index'))
flag = ""
for (index, part) in dictionary:
    flag += part
flag = F"picoCTF{{{flag}}}"
print(flag)
