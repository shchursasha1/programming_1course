def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


a, b = [int(el) for el in input().split()]
count = 0

for i in range(1, b + 1):
    if (a * b) % i == 0:
        if gcd((a * b) / i, i) == a and lcm((a * b) / i, i) == b:
            count += 1
    else:
        pass

print(count)
