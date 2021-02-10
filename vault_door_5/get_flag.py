import base64
import os
import re
from urllib.parse import unquote

link = 'https://jupiter.challenges.picoctf.org/static/9505cca05dc00fecead41106370ee619/VaultDoor5.java'

src = os.popen('curl -sL '+link).read()

based = src.replace("\n", "")
based = re.findall(r"boolean check.*return", based)
based = re.findall(r'".*"', based[0])[0].split("+")
based = [x.strip().replace('"', "") for x in based]

b64string = ''.join(based)
decoded = base64.decodebytes(b64string.encode('ascii')).decode('ascii')

decoded = unquote(decoded)

print("picoCTF{"+decoded + "}")
