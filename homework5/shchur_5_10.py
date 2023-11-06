n = int(input())
list1 = [int(el) for el in input().split()]
m = int(input())
list2 = [int(el) for el in input().split()]
unique_list = []

for item in list1:
    if item not in list2:
        unique_list.append(item)

print(len(unique_list))
print(*unique_list)