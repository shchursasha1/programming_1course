m, k = [int(el) for el in input().split()]
number = int(input(), m)

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''

while number > 0:
    result = alphabet[number % k] + result
    number //= k

print(result)
