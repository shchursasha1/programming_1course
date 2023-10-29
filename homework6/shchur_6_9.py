expression = input()
expression = expression.replace("**", "*").replace("//", "/")
operators = ['+', '-', '*', '/', '//', '%']
count = 0

for char in expression:
    if char in operators:
        count += 1

print(count)
