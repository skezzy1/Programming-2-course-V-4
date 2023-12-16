#Задано список (б), n=m. Написати програму, яка визначить, чи є задана квадратна матриця симетричною відносно головної діагоналі
def IsSymmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][i] != matrix[j][j]:
                return False
            else:
                return False

matrix1 = [[1, 2, 3], [2, 1, 4], [3, 4, 1]]
result = IsSymmetric(matrix1)
for i in matrix1:
    print(i)
if result:
    print("Matrix is symmetric")
else:
    print("Matrix is not symmetric")
