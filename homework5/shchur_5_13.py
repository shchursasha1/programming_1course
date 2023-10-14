n = int(input())
array1 = [float(el) for el in input().split()]
positive_numbers = 0
counter = 0

for el in array1:
    if el > 0:
        positive_numbers += el
        counter += 1

if positive_numbers != 0:
    result = positive_numbers/counter
    print(round(result, 2))

else:
    print("Not Found")
