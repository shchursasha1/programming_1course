"""
Модуль призначено для синтаксичного розбору виразу по частинах.

Вираз може мати вигляд:
(abc + 123.5)*d2-3/(x+y)
Вираз може містити:
    - змінні - ідентифікатори
    - константи - дійсні або цілі числа без знаку
    - знаки операцій: +, -, *, /
    - дужки: (, )

Функція `get_tokens` за заданим виразом має повертати послідовність 
лексем -- токенів.

Кожний токен (див. class Token) -- це пара: (<тип токену>, <значення токену>)
"""

# типи токенів
TOKEN_TYPE = (
    "variable",
    "constant",
    "operation",
    "equal",
    "left_paren",
    "right_paren",
    "other", 
)


# словник фіксованих токенів, що складаються з одного символа
TOKEN_TYPES = {
    "+": "operation",
    "-": "operation",
    "*": "operation",
    "/": "operation",
    "(": "left_paren",
    ")": "right_paren",
    "=": "equal",
}


class Token: 

    def __init__(self, type, value): 
        assert type in TOKEN_TYPE, 'недопустимий тип токена'
        self.type = type
        self.value = value 

    def __eq__(self, __value: object) -> bool:
        return self.type == __value.type and self.value == __value.value

    def __repr__(self): 
        return f"Token(type='{self.type}', value='{self.value}')"


def get_tokens(string):
    """Функція за рядком повертає список токенів типу Token.
    
    :param string: рядок
    :return: список токенів
    """
    tokens = []
    while string:
        token, string = _get_next_token(string)
        if token:
            tokens.append(token)
    return tokens


def _get_next_token(string):
    string = string.strip()  # Видаляємо пробіли в кінці та на початку рядка
    if not string:
        return None, ""

    # Перевіряємо, чи перший символ є фіксованим токеном
    if string[0] in TOKEN_TYPES:
        token_type = TOKEN_TYPES[string[0]]
        return Token(token_type, string[0]), string[1:]

    # Перевіряємо, чи перший символ є літерою (змінна)
    if string[0].isalpha():
        return _get_variable(string)

    # Перевіряємо, чи перший символ є цифрою (константа)
    if string[0].isdigit():
        return _get_constant(string)

    # Перевіряємо інші символи, якщо вони не відповідають жодному відомому токену
    return _get_other(string)


def _get_par(string):
    if string[0] == '(':
        return Token('left_paren', '('), string[1:]
    elif string[0] == ')':
        return Token('right_paren', ')'), string[1:]
    return None, string


def _get_operator(string):
    if string[0] in "+-*/":
        return Token('operation', string[0]), string[1:]
    return None, string


def _get_equal(string):
    if string[0] == '=':
        return Token('equal', '='), string[1:]
    return None, string


def _get_constant(string):
    constant = ''
    for char in string:
        if char.isdigit() or char == '.':
            constant += char
        else:
            break
    if constant:
        return Token('constant', constant), string[len(constant):]
    return None, string


def _get_variable(string):
    variable = ''
    for char in string:
        if char.isalnum() or char == '_':
            variable += char
        else:
            break
    if variable:
        return Token('variable', variable), string[len(variable):]
    return None, string


def _get_other(string):
    other = ''
    for char in string:
        if char.isalnum() or char in "+-*/()=":
            break
        other += char
    if other:
        return Token('other', other), string[len(other):]
    return None, string


if __name__ == "__main__":

    needed = [
        Token(type='left_paren', value='('),
        Token(type='left_paren', value='('),
        Token(type='left_paren', value='('),
        Token(type='variable', value='ab1_'),
        Token(type='operation', value='-'),
        Token(type='constant', value='345.56'),
        Token(type='right_paren', value=')'),
        Token(type='left_paren', value='('),
        Token(type='operation', value='*'),
        Token(type='operation', value='/'),
        Token(type='other', value='.'),
        Token(type='constant', value='2'),
        Token(type='other', value='{'),
        Token(type='variable', value='_cde23')
    ]

    success = (x := get_tokens("(((ab1_ - 345.56)(*/.2{_cde23")) == needed 
    if not success: 
        if len(x) != len(needed): 
            print(f'wrong amount of tokens. Expected: {len(needed)}, got: {len(x)}')
        for exp, real in zip(needed, x): 
            if exp != real: 
                print(f'Expected: {exp}, got {real}')
        

    needed = [
        Token(type='variable', value='x'),
        Token(type='equal', value='='),
        Token(type='left_paren', value='('),
        Token(type='variable', value='a'),
        Token(type='operation', value='+'),
        Token(type='variable', value='b'),
        Token(type='right_paren', value=')')
    ]

    success = success and (x := get_tokens("x = (a + b)")) == needed
    if not success: 
        if len(x) != len(needed): 
            print(f'wrong amount of tokens. Expected: {len(needed)}, got: {len(x)}')
        for exp, real in zip(needed, x): 
            if exp != real: 
                print(f'Expected: {exp}, got {real}')        

    print("Success =", success)