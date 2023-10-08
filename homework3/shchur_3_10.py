n_str = input()
result = ""

for char in n_str:
    digit = int(char)

    if digit % 2 == 0:
        digit += 1
    elif digit % 2 != 0:
        digit -= 1

    result = result + str(digit)

print(result)