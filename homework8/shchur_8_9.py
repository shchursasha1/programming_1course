number = int(input())

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''

while number > 0:
    result = alphabet[number % 13] + result
    number //= 13

print(result)
