import re
from requests import get
import base64

url = "https://login.mars.picoctf.net/"

r = get(url)

script_name = re.findall(r'<script src="(.*)"', r.text)[0]

r = get(url+script_name)

strings = re.findall(r'"(.*?)"', r.text)

flag = strings[-2]
padding_length = 3-len(flag) % 3
flag = flag + "=" * padding_length
flag = base64.b64decode(flag).decode()
print(flag)
