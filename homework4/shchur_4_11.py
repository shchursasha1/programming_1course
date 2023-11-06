list1 = []

while True:
    n = int(input())
    list1.append(n)
    if n == 0:
        break

print(sum(list1))