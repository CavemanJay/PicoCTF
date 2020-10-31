#!/usr/bin/python3
def read_file(path):
    with open(path) as file:
        return file.read()


index_file = './site/index.html'
js_file = './site/myjs.js'
css_file = './site/mycss.css'

part_one = [line for line in read_file(
    index_file).split() if line.startswith('pico')][0]

part_two = read_file(css_file).splitlines()[-1].split()[-2]
part_three = read_file(js_file).splitlines()[-1].split()[-2]

print(part_one+part_two + part_three)
