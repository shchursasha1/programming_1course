N = int(input("N = "))
array = [int(el) for el in input().split()]
count_elements = str(array).count(',') + 1

try:
    max_ratio = max(array[i] / array[i - 1] for i in range(1, len(array)))
except ZeroDivisionError:
    print("У послідовності є нульові елементи")
except Exception as e:
    print("Сталася невідома помилка: ", e)
else:
    print("c) Значення найбільшого відношення (частки) серед елементів = %f" % max_ratio)
    print(f"a) Кількість елемнтів у списку: {count_elements}")
    print(f"b) Сума елементів списку: {sum(array)}")
