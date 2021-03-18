from pwn import remote, context

host, port = "jupiter.challenges.picoctf.org", 41120
context.log_level = 100

r = remote(host, port)

print(r.recvall().decode().splitlines()[-1])

r.close()
