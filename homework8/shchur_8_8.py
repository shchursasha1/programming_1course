n = bin(int(input()))
output_string = ""

for char in n[2:]:
    if char == '1':
        output_string += 'SX'
    elif char == '0':
        output_string += 'S'

print(output_string[2:])

