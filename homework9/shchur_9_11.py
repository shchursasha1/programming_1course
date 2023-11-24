def clean_text(text):
    punctuation_marks = ['.', ',', ':', ';', '-', "'", '"', '!', '?']
    for mark in punctuation_marks:
        text = text.replace(mark, '')
    return text


N, M = map(int, input().split())
dictionary = {input().strip().lower() for _ in range(N)}

text_words = set()

for _ in range(M):
    current_text = input().lower()
    cleaned_text = clean_text(current_text)
    text_words.update(cleaned_text.split())

unknown_words = text_words - dictionary
missing_words = dictionary - text_words

if not unknown_words and not missing_words:
    print("Everything is going to be OK.")
elif unknown_words:
    print("Some words from the text are unknown.")
else:
    print("The usage of the vocabulary is not perfect.")
