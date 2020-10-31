from pwn import remote, context

# Credit to: https://stackoverflow.com/a/32094652
CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

CODE_REVERSED = {value: key for key, value in CODE.items()}


def to_morse(s):
    return ' '.join(CODE.get(i.upper()) for i in s)


def from_morse(s):
    out = ""
    for char in s.split():
        decoded = CODE_REVERSED.get(char)
        out += decoded if decoded is not None else char
    return out


# context.log_level = 100
context.log_level = 1

host, port = "jupiter.challenges.picoctf.org", 48247
r = remote(host, port)

# morse_code = '.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. .---- ..--- -.... .---- ....- ...-- ---.. .---- ---.. .---- }'
morse_code = r.recvall().decode()
print(from_morse(morse_code))
r.close()
