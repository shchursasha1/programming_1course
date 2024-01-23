from math import gcd

F = {}
MOD = 100000000

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n in F:
        return F[n]
    k = n // 2
    if n % 2 == 1:
        F[n] = (fib(k) * fib(k) + fib(k + 1) * fib(k + 1)) % MOD
    else:
        F[n] = (fib(k) * fib(k + 1) + fib(k - 1) * fib(k)) % MOD
    return F[n]

while True:
    try:
        a, b = map(int, input().split())
        print(fib(gcd(a, b)))
    except EOFError:
        break

