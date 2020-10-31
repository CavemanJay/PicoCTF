#!/usr/bin/python3
import os
link = "https://2019shell1.picoctf.com/problem/21519/"
js_link = link + "myjs.js"
css_link = link+"mycss.css"

part_one = os.popen(F"curl -s {link} | grep -oE pico.*").read().split(" ")[0]

part_two = os.popen(F"curl -s {css_link} | tail -n 1").read()
part_two = part_two[part_two.find("flag:")+5:].split(" ")[1]

part_three = os.popen(F"curl -s {js_link} | tail -n 1").read()
part_three = part_three[part_three.find("flag:")+5:].split(" ")[1]

flag = part_one+part_two+part_three
print(flag)
