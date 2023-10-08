n_str = input()
even_digits = 0

for char in n_str:
    digit = int(char)
    if digit % 2 == 0:
        even_digits += digit

if even_digits > 0:
    print(even_digits)
else:
    print(-1)