n = int(input())
list1 = [int(el) for el in input().split()]
unique_list = []

for item in list1:
    if item not in unique_list:
        unique_list.append(item)

print(*unique_list)
