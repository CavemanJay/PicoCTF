import binascii
import os
import re

link = "https://jupiter.challenges.picoctf.org/static/834acd392e0964a41f05790655a994b9/VaultDoor4.java"


src = os.popen('curl -sL '+link).read().replace("\n", "")

theBytes = re.findall(r'myBytes.*};', src)[0]
theBytes = re.findall(
    r'{.*}', theBytes)[0].replace("{", "").replace("}", "").split("    ")
theBytes = [b for b in theBytes if b != ""]

part1 = theBytes[0].replace(' ', '').split(',')
part1 = [int(num) for num in part1 if num != '']
part1 = ''.join([chr(n) for n in part1])

part2 = theBytes[1].replace(' ', '').split(',')
part2 = [hexStr for hexStr in part2 if hexStr != ""]
part2 = ''.join([chr(int(h, 16)) for h in part2])

part3 = theBytes[2].replace(' ', '').split(',')
part3 = ''.join([chr(int(octal, 8)) for octal in part3 if octal != ''])

part4 = theBytes[3].replace(' ', '').split(',')
part4 = ''.join([x.replace("'", '') for x in part4])

print('picoCTF{' + part1 + part2 + part3 + part4 + "}")
