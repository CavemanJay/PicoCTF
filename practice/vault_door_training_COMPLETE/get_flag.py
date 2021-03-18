#!/usr/bin/python3

with open('./VaultDoorTraining.java') as source_file:
    src = source_file.readlines()[-3]
    flag = src[src.find('"')+1:].split('"')[0]
    flag = F"picoCTF{{{flag}}}"
    print(flag)
