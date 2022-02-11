import re
from pwn import ELF, process, context
from icecream import ic

ic.disable()
context.log_level = "warn"

patched = "patched"
offset = 0x00100000
set_timer = 0x0010082f

elf = ELF('need-for-speed')

elf.address += offset

elf.asm(set_timer, "RET")
elf.save(patched)

p = process(F"chmod +x {patched} && ./{patched}", shell=True)
flag = ic(p.recvall().decode())
flag = re.findall(r'PICOCTF{.*?}',flag)[0]

print(flag)
