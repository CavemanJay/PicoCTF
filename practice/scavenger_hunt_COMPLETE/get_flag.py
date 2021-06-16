import re
import requests

url = "http://mercury.picoctf.net:27393/"
paths = ["mycss.css", "robots.txt", ".htaccess", ".DS_Store"]

flagParts = []

r = requests.get(url)
flagParts.append(re.findall("picoCTF{.", r.text)[0])

for path in paths:
    r = requests.get(url + path)
    flagPart = re.findall(r"Part \d: (.*)(?:\s)?", r.text,
                          re.IGNORECASE)[0].split(' ')[0]
    flagParts.append(flagPart)

flag = "".join(flagParts)
print(flag)
