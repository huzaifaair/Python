arr12 = np.random.randint(0, 50, (5, 5))
print(arr12)
print(np.var(arr12, axis=1))
print(np.var(arr12, axis=0))
print(np.min(arr12, axis=1))
print(np.min(arr12, axis=0))
print(np.max(arr12, axis=1))
print(np.max(arr12, axis=0))