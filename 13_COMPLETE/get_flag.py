cipher = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
chars_to_ignore = [95, 123, 125]
flag = ""

for c in cipher:
    asciiVal = ord(c)
    if asciiVal in chars_to_ignore:
        flag += c
    else:
        rotated = asciiVal+13
        while rotated > 122 or (rotated > 90 and rotated < 97):
            rotated -= 26
        flag += chr(rotated)
print(flag)
