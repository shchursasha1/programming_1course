count_runtime_errors = 0
count_type_errors = 0
count_value_errors = 0

while True:
    try:
        user_input = input("Введіть число або слово 'досить': ")

        if user_input.lower() == 'досить':
            break

        number = float(user_input)

        if number > 9:
            raise RuntimeError("Число більше 9")
        elif number < 0:
            raise TypeError("Число менше 0")
        elif 0 <= number >= 9:
            raise ValueError("Дійсне значення в діапазоні від 0 до 9")

    except RuntimeError as e:
        print(f"RuntimeError: {e}")
        count_runtime_errors += 1
    except TypeError as e:
        print(f"TypeError: {e}")
        count_type_errors += 1
    except ValueError as e:
        print(f"ValueError: {e}")
        count_value_errors += 1

print(f"Кількість RuntimeErrors: {count_runtime_errors}")
print(f"Кількість TypeErrors: {count_type_errors}")
print(f"Кількість ValueErrors: {count_value_errors}")
