def create_text_file(sequence, filename):
    with open(filename, 'w') as file:
        lines = [sequence[i:i+40] for i in range(0, len(sequence), 40)]

        for line in lines:
            file.write(line + '\n')


sequence = input("Задайте послідовність символів: ")

filename = "output.txt"
create_text_file(sequence, filename)