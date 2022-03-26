import r2pipe

r = r2pipe.open("./gdbme", ["-d", "-2"])
r.cmd('aaa') # analyze the binary
r.cmd('db main+99') # set a breakpoint before the sleep call
r.cmd('dc') # continue until the breakpoint
r.cmd('dr rdi=1') # change the value being passed to sleep

print(r.cmd('dc')) # continue and print flag
