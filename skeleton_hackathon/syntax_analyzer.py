from tokenizer import get_tokens, Token

# словник множин допустимих наступних токенів для заданого токена
VALID_PAIRS = {
    "variable": {"operation", "right_paren"},
    "constant": {"operation", "right_paren"},
    "operation": {"variable", "constant", "left_paren"},
    "equal": {"variable", "constant", "left_paren"},
    "left_paren": {"left_paren", "variable", "constant"},
    "right_paren": {"right_paren", "operation"},
    "other": set()
    }


# словник помилок
ERRORS = {
    "invalid_pair": "Недопустима пара токенів {}, {}",
    "incorrect_parens": "Неправильно розставлені дужки",
    "empty_expr": "Порожній вираз",
    "incorrect_assignment": "Неправильне присвоєння",
    "invalid_start": 'Недопустимий початок або кінець'
    }

# кортеж допустимих перших токенів
VALID_START = ('variable', 'constant', 'left_paren')

# кортеж допустимих останніх токенів
VALID_END = ('variable', 'constant', 'right_paren')


def check_assignment_syntax(tokens):
    """Функція перевіряє синтаксичну правильність присвоєння за списком токенів.

    Повертає True/False та рядок помилки.
    Якщо помилки немає, то повертає порожній рядок.
    Використовує функцію check_expression_syntax
    
    :param tokens: список токенів типу Token (див. tokenizer.py)
    :return: 
        success: булівське значення
        error: рядок помилки
    """
    if len(tokens) < 3:
        return False, ERRORS["incorrect_assignment"]

    if tokens[1].type != "equal":
        return False, ERRORS["incorrect_assignment"] 

    variable = tokens[0]
    expression_tokens = tokens[2:]

    success, error = check_expression_syntax(expression_tokens)
    if not success:
        return False, error

    return True, ""


def check_expression_syntax(tokens):
    """Функція перевіряє синтаксичну правильність виразу за списком токенів.

    Повертає True/False та рядок помилки.
    Якщо помилки немає, то повертає порожній рядок
    
    :param tokens: список токенів типу Token (див. tokenizer.py)
    
    :return:
        success: булівське значення
        error: рядок помилки
    """
    if not tokens:
        return False, ERRORS["empty_expr"]
    if not _check_start_end(tokens):
        return False, ERRORS["invalid_start"]
    if not _check_parens(tokens):
        return False, ERRORS["incorrect_parens"]
    for i in range(len(tokens) - 1):
        if not _check_pair(tokens[i], tokens[i + 1]):
            return False, ERRORS["invalid_pair"].format(tokens[i], tokens[i + 1])
    return True, ""


def _check_parens(tokens):
    """Функція перевіряє чи правильно розставлені дужки у виразі.
    
    Повертає True/False.
    :param tokens: список токенів
    :return: success - булівське значення
    """
    balance = 0

    for token in tokens:
        if token.type == "left_paren":
            balance += 1
        elif token.type == "right_paren":
            balance -= 1

        if balance < 0:
            break

    return not balance


def _check_pair(token, next_token):
    """Функція перевіряє чи правильна пара токенів.
    
    Повертає True/False.
    
    :param token: поточний токен
    :param next_token: наступний токен
    :return: success - булівське значення
    """
    return next_token.type in VALID_PAIRS[token.type]


def _check_start_end(tokens):
    """Функція перевіряє чи правильний токен стоїть на початку та кінці 
    заданого виразу.
    
    :param tokens: список токенів 
    :return: success -- True/False
    """
    if tokens[0].type not in VALID_START or tokens[-1].type not in VALID_END:
        return False
    return True


if __name__ == "__main__":
    success1, error1 = check_expression_syntax(get_tokens("(((ab1_ - 345.56)(*/.2{_cde23"))
    success2, error2 = check_expression_syntax(get_tokens("(ab1_ - 345.56)*/.2_cde23"))
    success3, error3 = check_expression_syntax(get_tokens(" - 345.56*/.2_cde23"))
    success4, error4 = check_expression_syntax(get_tokens("2 - 345.56 *"))
    success5, error5 = check_expression_syntax(get_tokens("2 - .2"))
    success6, error6 = check_expression_syntax(get_tokens("   "))
    success7, error7 = check_expression_syntax(get_tokens("((abc -3 * b2) + d5 / 7)"))
    success8, error8 = check_assignment_syntax(get_tokens("x + y"))
    success9, error9 = check_assignment_syntax(get_tokens("x ="))
    success10, error10 = check_assignment_syntax(get_tokens("x = (a+b)"))

    assert not success1 and error1 == 'Неправильно розставлені дужки'
    assert not success2 and error2 == "Недопустима пара токенів Token(type='operation', value='*'), Token(type='operation', value='/')" 
    assert not success3 and not success4 
    assert not success5 and error5 == "Недопустима пара токенів Token(type='operation', value='-'), Token(type='other', value='.')" 
    assert not success6 and error6 == "Порожній вираз" 
    assert success7 and error7 == "" 
    assert not success8 and error8 == "Неправильне присвоєння" 
    assert not success9 and error9 == "Порожній вираз" 
    assert success10 and error10 == ""
    
    print("Success =", True)
