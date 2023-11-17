def calculate_expression(expression):
    # Перевірка на незакриті дужки
    if expression.count('(') != expression.count(')'):
        raise ValueError("Незакриті дужки")

    # Щоб перевірка на ділення на -0 теж спрацьовувала
    expression = expression.replace('-0', '0')

    tokens = []
    current_token = ''
    for char in expression:
        if char.isdigit() or char == '.':
            current_token += char
        else:
            if current_token:
                tokens.append(float(current_token))
                current_token = ''
            if char != ' ':
                tokens.append(char)
    if current_token:
        tokens.append(float(current_token))

    def priority(operator):
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        else:
            return 0

    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            if right == 0:
                raise ZeroDivisionError("Ділення на нуль")
            values.append(left / right)

    operators = []  # Стек для операторів
    values = []  # Стек для значень

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if isinstance(token, float):
            values.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
        else:
            while operators and priority(operators[-1]) >= priority(token):
                apply_operator(operators, values)
            operators.append(token)
        i += 1

    while operators:
        apply_operator(operators, values)

    return values[0]


expression = input("Введіть математичний вираз: ")

try:
    result = calculate_expression(expression)
    print("Результат:", result)
except ZeroDivisionError as e:
    print("Помилка:", e)
except ValueError as e:
    print("Помилка:", e)
except Exception as e:
    print("Помилка:", e)
