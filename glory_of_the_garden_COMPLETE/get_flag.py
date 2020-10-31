import string
import re

# Running strings will work too lol
with open('./garden.jpg', errors="ignore") as img:
    data = img.read()
    flag = data.splitlines()[-1].split('"')[1]

    print(flag)
