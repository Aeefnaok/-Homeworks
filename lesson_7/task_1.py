class Matrix:
    def __init__(self, my_matrix):
        self.matrix = my_matrix

    def __str__(self):
        return '\n' + '\n'.join('\t'.join(map(str, line)) for line in self.matrix)

    def __add__(self, other):
        new_matrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                      for i in range(len(self.matrix))]
        return new_matrix


matrix_1 = [[2, 6, 9], [3, 8, 7], [1, 4, 5]]

matrix_2 = [[1, 4, 5], [3, 8, 7], [2, 6, 9]]

one = Matrix(matrix_1)
print(one)
two = Matrix(matrix_2)
print(two)
new = Matrix(one + two)
print(new)
