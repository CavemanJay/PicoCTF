from requests import get
import re

url = "http://mercury.picoctf.net:15472/"

r = get(url)
script_name = re.findall(r'<script src="(.*)"', r.text)[0]

r = get(url+script_name)
values = re.findall(r'\[.*?\]', r.text)[0]
values = re.findall(r"'(.*?)'", r.text)

wasm_script = [x for x in values if x.startswith("./")][0][2::]
r = get(url+wasm_script)

flag = re.findall(r"picoCTF{.*}", r.text)[0]
print(flag)
