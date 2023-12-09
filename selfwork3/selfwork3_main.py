import selfwork3_module


# Завдання a) - Перетворення матриці у верхню трикутну лінійними перетвореннями
def upper_triangular_form(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(len(matrix[i])):
                matrix[j][k] -= factor * matrix[i][k]

    return matrix


# Завдання б) - Визначення рангу матриці
def matrix_rank(matrix):
    rank = 0
    for i in range(len(matrix)):
        non_zero = False
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                non_zero = True
                break
        if non_zero:
            rank += 1

    return rank


# Завдання в) - Обчислення визначника матриці
def matrix_determinant(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Матриця не є квадратною")

    n = len(matrix)
    if n == 1:
        return matrix[0][0]

    determinant = 1
    for i in range(n):
        if matrix[i][i] == 0:
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    selfwork3_module.swap_rows(matrix, i, j)
                    determinant *= -1
                    break

        determinant *= matrix[i][i]

        factor = matrix[i][i]
        for j in range(i + 1, n):
            ratio = matrix[j][i] / factor
            for k in range(n):
                matrix[j][k] -= ratio * matrix[i][k]

    return determinant


A = selfwork3_module.input_matrix()
vector = selfwork3_module.input_vector()

upper_triangular_result = upper_triangular_form(A.copy())
print("Матриця у верхній трикутній формі:")
selfwork3_module.print_matrix(upper_triangular_result)

rank_A = matrix_rank(A)
print(f"Ранг матриці A: {rank_A}")

determinant_A = matrix_determinant(A)
print(f"Визначник матриці A: {determinant_A}")

matrix_minus_vector = selfwork3_module.subtract_vector_from_matrix(A, vector)
print("Результат віднімання вектора від всіх рядків матриці:")
selfwork3_module.print_matrix(matrix_minus_vector)