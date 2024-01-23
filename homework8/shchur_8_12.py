def PowMod(x, y, n):
    if y == 0:
        return 1
    if y & 1:
        return x * PowMod(x * x % n, y // 2, n) % n
    return PowMod(x * x % n, y // 2, n)


cs = 1
while True:
    k, n, t = map(int, input().split())
    if k + n + t == 0:
        break
    m = 1
    for i in range(t):
        m *= 10
    res = PowMod(k % m, n, m)
    print("Case #{}: {}".format(cs, res))
    cs += 1

