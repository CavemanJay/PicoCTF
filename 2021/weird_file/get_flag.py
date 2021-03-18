#!/usr/bin/python3
from oletools.olevba import VBA_Parser, TYPE_OLE
import base64

parser = VBA_Parser("weird.docm")

vba = parser.extract_all_macros()[0][3].split()

flag_line = None

for line in vba:
    if "print" in line:
        flag_line = line


encoded_flag = flag_line.split("\\")[1][1:]

decoded = base64.b64decode(encoded_flag).decode()

print(decoded)
