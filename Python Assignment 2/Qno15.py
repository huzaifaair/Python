arr13 = np.random.rand(3, 3)
np.savetxt("random_floats.txt", arr13)
loaded_arr = np.loadtxt("random_floats.txt")
print(loaded_arr)