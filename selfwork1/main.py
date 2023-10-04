n = int(input())
res_product = 1

for i in range(1, n + 1):
    if n > 8:
        if i % 8 == 0:
            res_product *= i
    else:
        print(0)

print(res_product)
