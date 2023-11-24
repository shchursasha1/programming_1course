def simple_addition(n):
    t = n % 10
    if n == 0:
        return 0
    return t * (1 + t) // 2 + n // 10 * 45 + simple_addition(n // 10)


def calculate_sum(p, q):
    return simple_addition(q) - simple_addition(p - 1)


while True:
    p, q = map(int, input().split())
    if p + q < 0:
        break
    print(calculate_sum(p, q))
