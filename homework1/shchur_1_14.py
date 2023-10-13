x, y = [float(d) for d in input().split()]
action1 = (2*x*y) / ((x**2 + y**2) ** 0.5)
action2 = ((x + y - 1)**2) / (x*y)
result = action1 - action2
print(round(result, 3))