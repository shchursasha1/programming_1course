n = int(input())

if n == 1:
    sum_even_digit_numbers = 0
    for number in range(100, 1000):
        digits = [int(digit) for digit in str(number)]
        if all(digit % 2 == 0 for digit in digits):
            sum_even_digit_numbers += number

    print(sum_even_digit_numbers)

elif n == 2:
    count_increasing_numbers = 0
    for number in range(100, 1000):
        digits = [int(digit) for digit in str(number)]
        if digits[0] < digits[1] < digits[2]:
            count_increasing_numbers += 1

    print(count_increasing_numbers)

elif n == 3:
    odd_numbers_sum = 0
    for number in range(100, 1000):
        digits = [int(digit) for digit in str(number)]
        if all(digit % 2 != 0 for digit in digits):
            odd_numbers_sum += number

    print(odd_numbers_sum)

elif n == 4:
    count_decreasing_numbers = 0
    for number in range(100, 1000):
        digits = [int(digit) for digit in str(number)]
        if digits[0] > digits[1] > digits[2]:
            count_decreasing_numbers += 1

    print(count_decreasing_numbers)

elif n == 5:
    cubic_digits_sum = 0
    for number in range(100, 1000):
        digits = [int(digit) for digit in str(number)]
        if number == sum(digit ** 3 for digit in digits):
            cubic_digits_sum += number

    print(cubic_digits_sum)

elif n == 6:
    different_digits_count = 0
    for number in range(100, 1000):
        digits = [int(digit) for digit in str(number)]
        if digits[0] != digits[1] and digits[1] != digits[2] and digits[0] != digits[2]:
            different_digits_count += 1

    print(different_digits_count)
