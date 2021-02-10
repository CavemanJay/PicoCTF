import os
import re
link = "https://jupiter.challenges.picoctf.org/static/eb5e6df8e14c52873cf88c582a1a4008/ciphertext"

src = os.popen('curl -sL ' + link).read()

n = re.findall('N:.*\n', src)[0].strip().replace("N: ", '')

e = re.findall('e:.*\n', src)[0].strip().replace('e: ', '')
c = re.findall('ciphertext.*', src)[0].strip().replace('ciphertext (c): ', '')

cmd = F'rsactftool -e {e} -n {n} --uncipher {c} 2>&1'

print(os.popen(cmd).read())
