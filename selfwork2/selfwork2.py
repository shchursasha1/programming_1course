# 5.71

text = input()
symbol = input()
max_char = ""
max_length = 0
cur_char = ""
cur_length = 1

if symbol in text:
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            cur_length += 1
        else:
            if cur_length > max_length:
                max_length = cur_length
                max_char = text[i - 1]
            cur_length = 1

    if cur_length > max_length:
        max_length = cur_length
        max_char = text[-1]

    print(f"Символ: {max_char}, Довжина найдовшої послідовності: {max_length}")

else:
    print(f"'{symbol}' немає в тексті.")
