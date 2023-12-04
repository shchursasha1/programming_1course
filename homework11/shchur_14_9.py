def read_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [float(num) for line in file for num in line.split()]
            return numbers
    except (IOError, ValueError) as e:
        print(f"Помилка читання файлу {file_path}: {e}")
        return []


content_file_path = 'content.txt'

try:
    with open(content_file_path, 'r') as content_file:
        file_list = content_file.read().splitlines()

        total_sum = 0

        for file_name in file_list:
            file_path = file_name + ".txt"

            try:
                with open(file_path, 'r') as file:
                    numbers = read_numbers_from_file(file_path)
                    total_sum += sum(numbers)
            except (IOError, PermissionError) as e:
                print(f"Помилка читання, або в доступі до файлу: {file_path}: {e}")

        print(f"Підсумовані дані, з файлів, що вказані у файлі {content_file_path}: {total_sum}")

except FileNotFoundError or FileExistsError:
    print(f"Помилка: {content_file_path} не знайдено, або його не існує.")
