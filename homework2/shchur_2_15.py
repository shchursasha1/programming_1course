a, b, c = [int(d) for d in input().split()]
if a != 0 and a <= 100 and b <= 100 and c <= 100:
    D = b**2 - 4*a*c
    if D < 0:
        print("No roots")
    elif D == 0:
        x = -b / (2*a)
        print("One root: " + str(x))
    else:
        x1 = (-b + D ** 0.5) / 2 * a
        x2 = (-b - D ** 0.5) / 2 * a
        if x1 < x2:
            print(f"Two roots: {x1, x2}")
        elif x1 > x2:
            print(f"Two roots: {x2, x1}")
else:
    exit()
