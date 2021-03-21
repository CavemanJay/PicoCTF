# Note: Analyze disk image using testdisk
# File found in /root

import re

with open('down-at-the-bottom.txt') as f:
    contents = f.readlines()

flag_lines = [line for i, line in enumerate(contents) if i in [2, 6, 10]]

flag = ""
for line in flag_lines:
    chars = [x.strip() for x in re.findall(r'(?<=\().+?(?=\))', line)]
    chars = ''.join(chars)
    flag += chars

print(flag)
