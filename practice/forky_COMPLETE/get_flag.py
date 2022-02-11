import re
from pwn import ELF
import numpy as np

import warnings
warnings.filterwarnings("ignore")

offset = 0x0010000

elf = ELF("vuln", False)
elf.address += offset

main = elf.functions['main']

main_diss = elf.disasm(main.address, main.size)
fork_call_pattern = r'call\s+0x103f0'
forks = re.findall(fork_call_pattern, main_diss, re.IGNORECASE)

initial_val = re.findall(
    r'mov.*?\[eax\],\s+(0x[\w\d]+)', main_diss.replace("\n", "\t"))[0]
initial_val = np.int32(int(initial_val, 16))

update_val = re.findall(r"lea.*?edx,.*?\+(0x.*?)\]",
                        main_diss.replace('\n', 't'))[0]
update_val = np.int32(int(update_val, 16))

processes = 1
for i, _ in enumerate(forks):
    processes *= 2

for i in range(processes):
    initial_val += update_val

print(F"picoCTF{{{initial_val}}}")
