def find_largest(num1, num2, num3):
    
    largest = max(num1, num2, num3)
    return largest

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

print("The largest number is:", find_largest(number1, number2, number3))
