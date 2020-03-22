#!/usr/bin/env python3
import base64

encoded = 'dGg0dF93NHNfczFtcEwz'
decoded = str(base64.b64decode(encoded))[1:].replace("'","")
print(decoded)
