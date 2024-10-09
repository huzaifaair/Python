def factorial(n):
    
    result = 1

    for i in range(1, n + 1):
        result *= i  
    
    return result

number = int(input("Enter a number to calculate its factorial: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {number} is: {factorial(number)}")
