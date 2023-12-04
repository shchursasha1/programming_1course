def solve_quadratic_equation(a, b, c):
    assert a != 0, "Коефіцієнт a повинен бути відмінним від нуля"

    discriminant = b**2 - 4*a*c

    assert discriminant >= 0, "Рівняння не має розв'язків на множині дійсних чисел"

    root1 = (-b + (discriminant**0.5)) / (2*a)
    root2 = (-b - (discriminant**0.5)) / (2*a)

    return root1, root2


a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

try:
    roots = solve_quadratic_equation(a, b, c)
    print("Розв'язки рівняння:", roots)
except AssertionError as e:
    print(f"Помилка: {e}")
