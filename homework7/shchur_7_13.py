a, b = [int(el) for el in input().split()]
result = []

for number in range(a, b + 1):
    digits = set(str(number))
    if len(digits) == 4:
        result.append(number)

print(*result)
