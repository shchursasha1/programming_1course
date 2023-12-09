def input_matrix():
    rows = int(input("Введіть кількість рядків матриці: "))
    cols = int(input("Введіть кількість стовпців матриці: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Введіть елемент [{i + 1},{j + 1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix


def input_vector():
    n = int(input(f"Вкажіть кількість елементів вектора: "))

    vector = []
    for i in range(n):
        element = float(input(f"Введіть елемент[{i}] = "))
        vector.append(element)
    return vector


def print_matrix(matrix):
    for row in matrix:
        print(row)


def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Множення двох матриць можливе тільки якщо кількість стовпців у матриці A дорівнює кількості рядків у матриці B.")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
            row.append(element)
        result.append(row)
    return result


def matrix_vector_multiplication(matrix, vector):
    if len(matrix[0]) != len(vector):
        raise ValueError("Неможливо помножити матрицю на вектор, кількість стовпчиків матриці не дорівнює довжині вектора.")

    result = []
    for row in matrix:
        new_element = sum(row[i] * vector[i] for i in range(len(vector)))
        result.append(new_element)

    return result


def vector_matrix_multiplication(vector, matrix):
    if len(vector) != len(matrix):
        raise ValueError("Неможливо помножити вектор на матрицю, довжина вектора не дорівнює кількості рядків матриці.")

    result = []
    for i in range(len(matrix[0])):
        new_element = sum(vector[j] * matrix[j][i] for j in range(len(vector)))
        result.append(new_element)

    return result


def swap_rows(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
    return matrix


def swap_columns(matrix, col1, col2):
    for i in range(len(matrix)):
        matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]
    return matrix


def get_row(matrix):
    row_index = int(input("Вкажіть номер рядка матриці, який бажаєте вивести: "))
    return matrix[row_index]


def scalar_vector_multiplication(vector):
    scalar = float(input("Введіть число, на яке бажаєте помножити вектор: "))
    return [scalar * element for element in vector]


def subtract_vector_from_matrix(matrix, vector):
    if len(matrix[0]) != len(vector):
        raise ValueError("Кількість елементів в рядках матриці менше, ніж кількість елементів вектора.")

    result = []
    for row in matrix:
        new_row = [element - vector[i] for i, element in enumerate(row)]
        result.append(new_row)

    return result


if __name__ == "__main__":
    A = input_matrix()
    print("Введена матриця:")
    print_matrix(A)

    B = input_matrix()
    print("Ще одна матриця:")
    print_matrix(B)

    C = matrix_multiplication(A, B)
    print("Результат множення матриць:")
    print_matrix(C)

    vector = input_vector()
    result_vector_matrix = vector_matrix_multiplication(vector, A)
    print("Результат множення вектора на матрицю:")
    print(result_vector_matrix)

    result_matrix_vector = matrix_vector_multiplication(A, vector)
    print("Результат множення матриці на вектор:")
    print(result_matrix_vector)

    A_swapped_rows = swap_rows(A.copy(), 0, 1)
    print("Матриця після перестановки рядків:")
    print_matrix(A_swapped_rows)

    A_swapped_columns = swap_columns(A.copy(), 0, 1)
    print("Матриця після перестановки стовпчиків:")
    print_matrix(A_swapped_columns)

    row_result = get_row(A.copy())
    print(f"Рядок матриці: {row_result}")

    scalar_vector_result = scalar_vector_multiplication(vector)
    print(f"Результат множення вектора на число: {scalar_vector_result}")

    vector = [1, 2, 3]
    matrix_minus_vector = subtract_vector_from_matrix(A.copy(), vector)
    print("Результат віднімання вектора від всіх рядків матриці:")
    print_matrix(matrix_minus_vector)
