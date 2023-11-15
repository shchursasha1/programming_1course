a = input()
b = input()

unique_chars_a = set(a)
unique_chars_b = set(b)

contains_all_chars = [True if n in unique_chars_a else False for n in unique_chars_b]
all_chars_present = all(contains_all_chars)

if all_chars_present:
    print("Ok")
else:
    print("No")

