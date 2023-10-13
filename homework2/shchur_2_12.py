x = int(input())
if -1000 <= x <= 1000:
    if x >= 0:
        y = x**3 + 2*x**2 + 4*x - 6
        print(y)
    elif x < 0 and x != 0:
        y = x**3 - 7*x
        print(y)
else:
    exit()
