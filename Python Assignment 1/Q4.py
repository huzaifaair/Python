# Function to calculate the grade based on marks
def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    elif marks >= 50:
        return 'E'
    else:
        return 'F'

# Taking marks input from the user
marks = float(input("Enter the marks obtained (0-100): "))

# Validate if marks are within the correct range
if marks < 0 or marks > 100:
    print("Invalid marks. Please enter a value between 0 and 100.")
else:
    # Calculate and print the grade
    grade = calculate_grade(marks)
    print(f"The grade for marks {marks} is: {grade}")
