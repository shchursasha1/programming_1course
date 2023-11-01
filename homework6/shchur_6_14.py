string = input()
string_without_spaces = string.replace(" ", "")

if string_without_spaces == string_without_spaces[::-1]:
    print("YES")
else:
    print("NO")


