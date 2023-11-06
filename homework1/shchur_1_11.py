import math
a, b, c, d, f = [float(d) for d in input().split()]
half_perimetr1 = (a + b + f) / 2
half_perimetr2 = (f + d + c) / 2
s_triangle1 = (half_perimetr1*(half_perimetr1 - a)*(half_perimetr1 - b)*(half_perimetr1 - f))**(1/2)
s_triangle2 = (half_perimetr2*(half_perimetr2 - f)*(half_perimetr2 - d)*(half_perimetr2 - c))**(1/2)
s_quadrangle = s_triangle1 + s_triangle2

print(round(s_quadrangle, 4))