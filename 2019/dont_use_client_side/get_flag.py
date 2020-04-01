#!/usr/bin/python3
import os
from collections import namedtuple
from operator import attrgetter
src = os.popen(
    "curl -s https://2019shell1.picoctf.com/problem/49886/ | head -n 20 | tail -n 8").read()
lines = []
for x, line in enumerate(src.split("\n")):
    lines.append(line.lstrip())

FlagPart = namedtuple('FlagPart', ['index', 'part'])


def get_index(line: str):
    star_index = line.find("*")
    result = line[star_index+1:star_index+2]
    if star_index == -1:
        return 0
    if star_index == 36:
        return 1
    return int(result)


def get_flag_part(line: str):
    return line.split("'")[1]


def sort_named_tuple_list(the_list: list, field_name: str):
    return sorted(the_list, key=attrgetter(field_name))


lines.pop(8)
dictionary = []
for line in lines:
    index = get_index(line)
    part = get_flag_part(line)
    dictionary.append(FlagPart(index, part))

dictionary = sort_named_tuple_list(dictionary, 'index')
flag = ""
for flag_part in dictionary:
    flag += flag_part.part
print(flag)
