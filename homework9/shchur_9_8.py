n = int(input())
input_list = [int(el) for el in input().split()]
unique_list = set(input_list)
result_list = []

counter = 0

for num in unique_list:
    result_list.append(abs(num))

print(len(set(result_list)))

