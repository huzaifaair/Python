arr10 = np.array([[1, 2, 3], [4, 5, 6]])
arr11 = np.array([[7, 8, 9], [10, 11, 12]])
vertical_concat = np.vstack((arr10, arr11))
horizontal_concat = np.hstack((arr10, arr11))
print(vertical_concat)
print(horizontal_concat)