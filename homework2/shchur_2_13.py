side1, side2, side3 = [int(el) for el in input().split()]
if side1 <= 100 and side2 <= 100 and side3 <= 100:
    if side1 == side2 == side3:
        print("1")
    elif side1 == side3 and side2 != side1 and side2 != side3:
        print("2")
    else:
        print("3")
else:
    exit()
