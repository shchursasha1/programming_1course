def check_crypto_strength(password):
    criteria = 0

    if any(character.islower() for character in password):
        criteria += 1

    if any(character.isupper() for character in password):
        criteria += 1

    if any(character.isdigit() for character in password):
        criteria += 1

    special_characters = "!\"#$%&'()*+"
    if any(character in special_characters for character in password):
        criteria += 1

    if len(password) >= 8:
        criteria += 1

    return criteria


password = input()
print(check_crypto_strength(password))
