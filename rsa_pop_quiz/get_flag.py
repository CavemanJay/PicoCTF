#!/usr/bin/python3

from math import gcd

from pwn import remote, context
import re


def compute_n(p: int, q: int):
    return str(p * q)


def compute_q(p: int, n: int):
    return str(int(n/p))

# totient of n: https://www.dcode.fr/euler-totient


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
t = totient(int(n))
print(t)

r.interactive()
r.close()
