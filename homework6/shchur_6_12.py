def decrypt_caesar_cipher(encryption, k):
    decrypted_text = ""
    for char in encryption:
        if char.isalpha():
            char_code = ord(char)

            is_upper = char.isupper()

            char_code -= k

            if is_upper and char_code < ord('A'):
                char_code += 26
            elif not is_upper and char_code < ord('a'):
                char_code += 26

            decrypted_char = chr(char_code)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text


encryption = input()
k = int(input())
decrypted_text = decrypt_caesar_cipher(encryption, k)

print(decrypted_text)


