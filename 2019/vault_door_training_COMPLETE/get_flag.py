#!/usr/bin/python3
import os

flag = os.popen(
    "curl -s https://2019shell1.picoctf.com/static/0a9478bb281651d883f8148672560fa1/VaultDoorTraining.java | tail -n 3 | head -n 1").read()
flag = flag[flag.find('"')+1:].split('"')[0]
flag = F"picoCTF{{{flag}}}"
print(flag)
