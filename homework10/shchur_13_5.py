def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    n = len(nums)
    list_lengths = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j] and list_lengths[i] < list_lengths[j] + 1:
                list_lengths[i] = list_lengths[j] + 1

    return max(list_lengths)


input_file_name = input("Введіть назву текстового файлу: ")

if ".txt" in input_file_name:
    with open(input_file_name) as my_file:
        content = my_file.read()
else:
    with open(input_file_name + ".txt") as my_file:
        content = my_file.read()

numbers = [int(num) for num in content.split()]
even_numbers = []
odd_numbers = []
odd_squares_in_content = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

for num in numbers:
    if num % 3 == 0:
        odd_numbers.append(num)

for num in numbers:
    if num % 2 != 0 and int(num**0.5)**2 == num:
        odd_squares_in_content.append(num)

print(f"a) Кількість парних чисел серед компонент: {len(even_numbers)}")
print(f"b) Кількості квадратів непарних чисел серед компонент: {len(odd_squares_in_content)}")
print(f"c) Різниця між найбільшим парним і найменшим непарним числами з компонент: {max(even_numbers) - min(odd_numbers)}")
print(f"d) Довжина найдовшої зростаючої послідовності: {longest_increasing_subsequence(numbers)}")