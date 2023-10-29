string = input()

letters = [char for char in string if char.isalpha and char.isascii()]
sorted_letters = sorted(letters)

print(''.join(sorted_letters))
