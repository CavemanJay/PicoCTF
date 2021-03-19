
import hashlib
from cryptography.fernet import Fernet
import base64
import string
import itertools

username_trial = "FREEMAN"
bUsername_trial = b"FREEMAN"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + \
    key_part_dynamic1_trial + key_part_static2_trial


salt = 'xxxxxxxx'
sequence = [4, 5, 3, 6, 2, 7, 1, 8]
hash = hashlib.sha256(bUsername_trial).hexdigest()

# All check_key is doing is comparing the value of the key to a specific index of the hash
for i in sequence:
    salt = salt.replace("x", hash[i], 1)

print(key_part_static1_trial+salt+key_part_static2_trial)
