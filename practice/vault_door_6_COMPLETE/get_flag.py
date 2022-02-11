import re
from icecream import ic
ic.disable()

with open('VaultDoor6.java', 'r') as f:
    source = f.read()

myBytes = re.findall(
    r'byte\[\] myBytes = \{(.*?)\}', source.replace("\n", ""))[0]
myBytes = re.sub(r'\s', '', myBytes).split(',')[0:-1]
myBytes = map(lambda x: int(x, 16), myBytes)
password = map(lambda b: chr(b ^ 0x55), myBytes)
flag = ic(F"picoCTF{{{''.join(password)}}}")

print(flag)
