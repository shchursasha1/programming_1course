def count_ones_in_range(n):
    count = 0
    k = 1
    while n >= k:
        a = n // (k * 2)
        b = n % (k * 2)
        count += a * k
        count += max(0, b - k + 1)
        k *= 2
    return count


a, b = [int(el) for el in input().split()]

count_a = count_ones_in_range(a - 1)
count_b = count_ones_in_range(b)
total_ones = count_b - count_a

print(total_ones)
