import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_lucky_prime(n):
    reverse_n = int(str(n)[::-1])
    return is_prime(n) and is_prime(reverse_n) and n != reverse_n


def find_k_lucky_prime(K):
    count = 0
    i = 2
    while count < K:
        if is_lucky_prime(i):
            count += 1
        i += 1
        if i > 1000000:
            return -1
    return i - 1


K = int(input())
result = find_k_lucky_prime(K)
print(result)


