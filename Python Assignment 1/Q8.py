def fibonacci(n):
    a, b = 0, 1
    
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print(f"Fibonacci sequence up to {n} term: {a}")
    else:
        print("Fibonacci sequence:")
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b   

num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

fibonacci(num_terms)
