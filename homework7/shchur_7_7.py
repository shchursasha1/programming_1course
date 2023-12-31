def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


n = int(input())
result = 1

for i in range(1, n + 1):
    result = lcm(result, i)

print(result)

