from icecream import ic
ic.disable()

with open('rev_this', 'r') as f:
    encoded_flag = f.readline().strip()[8:-1]

ic(encoded_flag)


def decode_flag(encoded_flag: str):
    for index, char in enumerate(encoded_flag):
        if index % 2 == 0:
            yield ic(chr(ord(char)-ord('\x05')))
        else:
            yield ic(chr(ord(char)+2))


decoded = ic("".join(decode_flag(encoded_flag)))
print(F"picoCTF{{{decoded}}}")
