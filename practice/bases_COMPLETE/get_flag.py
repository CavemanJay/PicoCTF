#!/usr/bin/python3
import base64
cipher = "bDNhcm5fdGgzX3IwcDM1"
flag = str(base64.b64decode(cipher)).split("'")[1]
flag = F"picoCTF{{{flag}}}"
print(flag)
