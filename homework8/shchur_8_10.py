import itertools

n = int(input())
my_list = []

for i in range(1, n + 1):
    my_list.append(i)

permutations = list(itertools.permutations(my_list))

for p in permutations:
    print(*p)
