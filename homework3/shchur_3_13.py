import math

n = int(input())

res = 0
for i in range(1, n + 1):
    res += math.log10(i)

print(int(res) + 1)
