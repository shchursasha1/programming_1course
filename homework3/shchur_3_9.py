n = int(input())
j = 0
number = 1
while j < n:
    if number % 2 != 0 and number % 3 != 0 and number % 5 != 0:
        j = j + 1
        print(number, end=" ")
    number = number + 1