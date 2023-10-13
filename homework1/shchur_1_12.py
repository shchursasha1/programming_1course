x1, y1, x2, y2, alpha = [float(d) for d in input().split()]
x = (x1 + (x2 * alpha)) / (1 + alpha)
y = (y1 + (y2 * alpha)) / (1 + alpha)
print(f"{x:.2f} {y:.2f}")
