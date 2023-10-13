number = int(input())
action1 = number // 10
first_digit = action1 // 10
second_digit = action1 % 10
third_digit = number % 10
list1 = [first_digit, third_digit]

if first_digit != third_digit:
    print(max(list1))
else:
    print("=")
