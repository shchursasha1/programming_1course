list1 = []

while True:
    n = int(input())
    if n == 0:
        break
    elif n % 2 == 0:
        list1.append(n)

print(sum(list1))
