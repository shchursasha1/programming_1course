a, b, c, d = [int(el) for el in input().split()]
temp_list = []
unique_result_list = []

for i in range(a, b + 1):
    for j in range(c, d + 1):
        temp_list.append(i * j)


for item in temp_list:
    if item not in unique_result_list:
        unique_result_list.append(item)


print(len(unique_result_list))
