N = int(input())
dictionary = {}
result_dictionary = {}

for _ in range(N):
    input_string = input()
    lines = input_string.split('\n')

    for line in lines:
        parts = line.split(' - ')
        if len(parts) == 2:
            key, values_str = parts
            values = values_str.split(', ')
            dictionary[key] = values


for key, possible_values in dictionary.items():
    if isinstance(possible_values, str):
        possible_values = [possible_values]

    for value in possible_values:
        if value not in result_dictionary:
            result_dictionary[value] = []

        result_dictionary[value].append(key)

sorted_keys = sorted(result_dictionary.keys())

print(len(result_dictionary))
for key in sorted_keys:
    values = ', '.join(sorted(result_dictionary[key]))
    print(f"{key} - {values}")