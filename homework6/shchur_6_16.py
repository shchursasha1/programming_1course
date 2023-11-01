s = input()

letters = [char for char in s if char.isalnum]

print(letters[2] + letters[6] + letters[10])  # 1
print(letters[0] + letters[len(letters) - 2] + letters[len(letters) - 1])  # 2
print(s[0:7])  # 3
print(s[4:])  # 4
odd_slice = s[1:len(s):2]
print(odd_slice)  # 5
print(len(odd_slice))  # 6
print(s[::-1])  # 7
