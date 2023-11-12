def is_palindrome(s):
    return s == s[::-1]


def to_base_n(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result


n = int(input())


valid_bases = []
for base in range(2, 37):
    representation = to_base_n(n, base)
    if is_palindrome(representation):
        valid_bases.append(base)

if len(valid_bases) == 0:
    print("none")
elif len(valid_bases) == 1:
    print("unique")
    print(valid_bases[0])
else:
    print("multiple")
    print(" ".join(map(str, valid_bases)))
