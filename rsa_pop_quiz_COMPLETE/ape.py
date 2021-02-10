#!/usr/bin/python3

# relies on https://github.com/Ganapati/RsaCtfTool

from math import gcd

from pwn import remote, context
import re
import os
import subprocess


def compute_n(p: int, q: int):
    return str(p * q)


def compute_q(p: int, n: int):
    return str(int(n/p))

# totient of n: https://www.dcode.fr/euler-totient


def inverse(x, m):
    a, b, u = 0, m, 1
    while x > 0:
        q = b // x
        x, a, b, u = b % x, u, x, a-q*u
    if b == 1:
        return a % m
    raise ArithmeticError("Must be coprime")


def decrypt(c, d, n):
    return pow(c, d, n)


def encrypt(m: int, e: int, n: int):
    Me = m**e
    return Me % n


def get_value(val, prompt):
    return int(re.findall(val + ' : .*', prompt)[0].split()[-1])


def is_coprime(x, y):
    return gcd(x, y) == 1

# https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-120.php


def totient(n):
    amount = 0
    for k in range(1, n + 1):
        print(f'{k} of {n}')
        if gcd(n, k) == 1:
            amount += 1
    return amount


def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
    return gcd, x, y


host, port = "jupiter.challenges.picoctf.org", 1981

r = remote(host, port)

prompt = r.recvuntil("IS THIS POSSIBLE").decode()
r.sendline('y')

q = get_value('q', prompt)
p = get_value('p', prompt)


r.sendline(compute_n(p, q))

prompt = r.recvuntil("IS THIS POSSIBLE").decode()

p = get_value('p', prompt)
n = get_value('n', prompt)

r.sendline('y')
q = compute_q(p, n)

r.sendline(q)

r.recvuntil("IS THIS POSSIBLE")
r.sendline('n')

prompt = r.recvuntil("IS THIS POSSIBLE").decode()

p = get_value('p', prompt)
q = get_value('q', prompt)

n = compute_n(p, q)
r.sendline('y')
# t = totient(int(n))
t = os.popen("g++ totient.cpp && ./a.out " + n).read()
r.sendline(t)

prompt = r.recvuntil("IS THIS POSSIBLE").decode()

r.sendline('y')

e = get_value('e', prompt)
n = get_value('n', prompt)
m = get_value('plaintext', prompt)
c = encrypt(m, e, n)
r.sendline(str(c))

r.recvuntil("IS THIS POSSIBLE")
r.sendline('n')

prompt = r.recvuntil("IS THIS POSSIBLE").decode()
r.sendline('y')

q = get_value('q', prompt)
p = get_value('p', prompt)
e = get_value('e', prompt)
phi = (p-1) * (q-1)
gcd, d, _ = egcd(e, phi)

r.sendline(str(d))

prompt = r.recvuntil("IS THIS POSSIBLE").decode()
r.sendline('y')

c = get_value('ciphertext', prompt)
e = get_value('e', prompt)
n = get_value('n', prompt)
p = int(get_value('p', prompt))
# q = int(compute_q(p, n))

r.close()

cmd = f"rsactftool -p {p} -n {n} -e {e} --uncipher {c}"

subprocess.Popen(cmd.split())

os.system('rm a.out')
