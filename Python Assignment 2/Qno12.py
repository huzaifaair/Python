zeros_matrix = np.zeros((5, 5))
ones_matrix = np.ones((3, 3))
zeros_matrix[1:4, 1:4] = ones_matrix
print(zeros_matrix)