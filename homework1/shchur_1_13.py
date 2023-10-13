x, y = [float(d) for d in input().split()]
action1 = (x**2) - (2*x*y) + (4*(y**2))
action2 = action1 / (x + 5)
action3 = ((3*(x**2)) - (y**2)) / (y - 7)
result = action2 + action3
print(round(result, 3))