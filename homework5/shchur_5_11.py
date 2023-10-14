n = int(input())
array1 = [int(el) for el in input().split()]
last_element = array1[-1]

for i in range(len(array1) - 1, 0, -1):
    array1[i] = array1[i - 1]

array1[0] = last_element

print(*array1)
