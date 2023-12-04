def task_a(input_filename):
    with open(input_filename, 'r') as input_file:
        content = input_file.read()
        words = content.split()

    print(f"Найдовше слово у файлі: {max(words)}")


task_a('13_7.txt')


def task_b(input_filename):
    with open(input_filename, 'r') as input_file:
        content = input_file.read()
        words = content.split()

    print(f"Кількість слів у файлі: {len(words)}")


task_b('13_7.txt')


def task_c(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            words = line.split()
            filtered_words = [word for word in words if len(word) > 1]
            cleaned_line = ' '.join(filtered_words)
            print(cleaned_line)
            output_file.write(cleaned_line + '\n')


task_c('13_7.txt', 'H.txt')


def task_d(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            cleaned_line = ' '.join(line.split())
            output_file.write(cleaned_line + '\n')


task_d('13_7.txt', 'H.txt')


def task_e(input_file, output_file='H_test1.txt', required_length=80):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        for line in lines:
            words = line.strip().split()

            if len(words) == 1:  # Якщо тільки одне слово, записуємо без змін
                f.write(line)
                continue

            words_amount = len(words)
            targets = words_amount + 1

            current_length = len(''.join(words))
            needed = required_length - current_length

            min_amount = needed // targets
            leftovers = needed % targets
            res = ' ' * min_amount

            if leftovers:
                res += ' '
                leftovers -= 1

            for word in words:
                res += word
                res += ' ' * min_amount
                if leftovers:
                    res += ' '
                    leftovers -= 1

            f.write(res + '\n')


task_e('13_7.txt', 'H.txt')
