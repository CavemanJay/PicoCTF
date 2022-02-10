#!/usr/bin/env python

import re
from pwn import ELF
from icecream import ic

ic.disable()
elf = ELF("./svchost.exe",False)

offset = 0x00100000
main = 0x0010298a
flag_build_start = 0x0010299d
flag_build_end = 0x00102a24

elf.address += offset


def get_char(func_addr: str):
    addr = int(func_addr, 16)
    dis = elf.disasm(addr, 24)
    char_addr = re.findall(r'#\s+(0x[\w\d]+)', dis)[0]
    return ic(elf.read(int(char_addr, 16), 1).decode())


flag_build_asm = elf.disasm(flag_build_start, flag_build_end-flag_build_start)

functions = re.findall(r'call\s+(0x.*)', flag_build_asm)
flag = "".join(map(get_char, functions))
print(flag)
