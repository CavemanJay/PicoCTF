#!/usr/bin/python3
import os
main_link = "https://2019shell1.picoctf.com/problem/4159/"
robots = os.popen(F"curl -s {main_link + 'robots.txt'}").readlines()
next_link = robots[1].split(" ")[1][1:].replace("\n", "")

command = F"curl -s {main_link + next_link} | grep -oE picoCTF{{.*}}"
flag_src = os.popen(command).read()
print(flag_src)
