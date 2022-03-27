import r2pipe

# Open the binary in debug mode with the specified profile (so we can pass something to stdin) and hide stderr
r = r2pipe.open("keygenme", flags=[
                '-d', '-e', 'dbg.profile=profile.rr2', '-2'])

# Analyze the binary
r.cmd('aaa') 
# Seek to main
r.cmd('s main')
# Find the address of the function that checks our input with the actual flag
address = r.cmd('/ad call~call 0x').split(" ")[-1].strip()

# Create a flag at that address and define it as a function
r.cmd(F'f check_license @ {address}')
r.cmd('af @ check_license')

# Move to the check_license function/flag
r.cmd('s check_license')

# Find the address where we compare the length of stdin with the length of the flag
address = r.cmd('/ad cmp rax, 0x24').split(" ")[0]
# Place a breakpoint at the address and then continue
r.cmd(F'db {address}')
r.cmd('dc')

# Print a string off the stack
print(r.cmd('ps @ rbp-0x30')[:0x24])
