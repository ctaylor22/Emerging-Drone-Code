MOD = 1 << 16

def ones_comp_add16(num1,num2):
    result = num1 + num2
    return result if result < MOD else (result+1) % MOD

f = open("num.txt")

lines = f.readlines()

i = 0
while i < len(lines):
    lines[i] = lines[i].strip("\n")
    i += 1

total = 0
for num in lines:
    total = ones_comp_add16(total, int(num, 16))


print(hex(int(hex(0xFFFF), 16) - int(hex(total), 16)))