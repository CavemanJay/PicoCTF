import binascii
import re
link = "https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery"


properHeader = b'89504e470d0a1a0a0000000d49484452'
headerLength = len(properHeader)

with open('mystery', 'rb') as f:
    content = f.read()

original = binascii.hexlify(content)
withoutHead = original[headerLength:]

fixed = properHeader + withoutHead


with open('fixed.png', 'wb') as f:
    f.write(binascii.unhexlify(fixed))
