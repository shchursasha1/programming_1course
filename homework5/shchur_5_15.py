n = int(input())
array = [int(el) for el in input().split()]

max_value = max(array)
min_value = min(array)

for i in range(len(array)):
    if array[i] == max_value:
        array[i] = min_value
    elif array[i] == min_value:
        array[i] = max_value

print(*array)
