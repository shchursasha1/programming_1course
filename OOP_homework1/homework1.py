import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            p = (self.a + self.b + self.c) / 2
            return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        else:
            return 0 # Якщо трикутник не існує, повертаємо 0


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def area(self):
        return self.length * self.width

class Trapeze:
    def __init__(self, base1, base2, side1, side2):
        self.base1 = base1
        self.base2 = base2
        self.side1 = side1
        self.side2 = side2
    
    def perimeter(self):   
        return self.base1 + self.base2 + self.side1 + self.side2

    # Пошук площі (без наявної інформації висоти) через чотири сторони
    def area(self):
        try:
            return ((self.base1 + self.base2) / 2) * math.sqrt((self.side1**2) - (((self.base1 - self.base2)**2 + self.side1**2 - self.side2**2)) / (2*(self.base1 - self.base2)) ** 2)
        except ValueError: # Якщо трапеція з заданими параметрами не існує - неможливо буде порахувати площу через помилку взяття кореня з від'ємного числа
            return 0
        except ZeroDivisionError:
            return 0
            
class Parallelogram:
    def __init__(self, base, side, height):
        self.base = base
        self.height = height
        self.side = side
    
    def perimeter(self):
        return 2 * (self.base + self.side)
    
    def area(self):
        return self.base * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * self.radius ** 2


# Функція для зчитування вхідних даних з файлу
def read_input(filename):
    figures = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split()
            figure_type = data[0]
            parameters = list(map(float, data[1:]))
            figures.append((figure_type, parameters))
    return figures


figures_data = []
for filename in ["input01.txt", "input02.txt", "input03.txt"]:
    figures_data.extend(read_input(filename))

max_area = 0
max_perimeter = 0
max_area_figure = None
max_perimeter_figure = None

for figure_type, parameters in figures_data:
    if figure_type == 'Triangle':
        triangle = Triangle(*parameters)
        area = triangle.area()
        perimeter = triangle.perimeter()
    elif figure_type == 'Rectangle':
        rectangle = Rectangle(*parameters)
        area = rectangle.area()
        perimeter = rectangle.perimeter()
    elif figure_type == 'Trapeze':
        trapezoid = Trapeze(*parameters)
        area = trapezoid.area()
        perimeter = trapezoid.perimeter()
    elif figure_type == 'Parallelogram':
        parallelogram = Parallelogram(*parameters)
        area = parallelogram.area()
        perimeter = parallelogram.perimeter()
    elif figure_type == 'Circle':
        circle = Circle(*parameters)
        area = circle.area()
        perimeter = circle.circumference()
    
    if area > max_area:
        max_area = area
        max_area_figure = (figure_type, area)
    
    if perimeter > max_perimeter:
        max_perimeter = perimeter
        max_perimeter_figure = (figure_type, perimeter)
    
    if area == 0:
        print(f'Фігура {figure_type} з параметрами {parameters} не існує.')
    
    if perimeter == 0:
        print(f'Фігура {figure_type} з параметрами {parameters} не існує.')

print("Фігура з найбільшою площею:", max_area_figure)
print("Фігура з найбільшим периметром:", max_perimeter_figure)
