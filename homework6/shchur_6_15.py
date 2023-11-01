string = input().split()
longest_word = ''
champion_word_index = -1


def is_palindrome(word):
    return word == word[::-1]


for i in range(len(string)):
    string[i] = ''.join(filter(str.isalnum, string[i]))

string = list(filter(None, string))

for j, word in enumerate(string):
    if is_palindrome(word) and len(word) > len(longest_word):
        longest_word = word
        champion_word_index = j

if champion_word_index != -1:
    print(champion_word_index + 1)
else:
    exit()
