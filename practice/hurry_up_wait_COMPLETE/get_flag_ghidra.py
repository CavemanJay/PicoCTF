# Script taken from: https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/Hurry_up_Wait.md
import sys
def getAddress(offset):
    return currentProgram.getAddressFactory().getDefaultAddressSpace().getAddress(offset)

listing = currentProgram.getListing()
functionManager = currentProgram.getFunctionManager()

main_func = getGlobalFunctions("FUN_0010298a")[0]

# Iterate the instructions that FUN_0010298a() is composed of
for codeUnit in listing.getCodeUnits(main_func.getBody(), True):

	if not codeUnit.toString().startswith("CALL"):
        # Ignore anything that isn't a "call"
		continue

	callee = functionManager.getFunctionAt(getAddress(str(codeUnit.getAddress(0))))
	if not callee.getName().startswith("FUN_"):
        # In practice - skip ada__calendar__delays__delay_for()
		continue

	for cu in listing.getCodeUnits(callee.getBody(), True):
        # Iterate the instructions that the callee is composed of
		if (not cu.toString().startswith("LEA RAX")):
            # Ignore anything that isn't LEA RAX, [addr]
            #  since that's the instruction that loads the flag character to be printed
			continue
		
        # Check what's at "addr" and print it
		sys.stdout.write(chr(getByte(getAddress(str(cu.getScalar(1))))))

print("")