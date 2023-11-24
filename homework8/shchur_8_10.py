def permutations(elements):
    if len(elements) <= 1:
        yield elements
        return

    for perm in permutations(elements[1:]):
        for i in range(len(elements)):
            yield perm[:i] + elements[0:1] + perm[i:]


n = int(input())
my_list = [str(j) for j in range(1, n + 1)]

for perm in sorted(permutations(my_list)):
    print(' '.join(perm))
