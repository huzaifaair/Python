def find_largest_and_smallest(numbers):
    if not numbers: 
        return None, None  

    smallest = min(numbers)
    largest = max(numbers)

    return smallest, largest

user_input = input("Enter numbers separated by spaces: ")

number_list = [float(num) for num in user_input.split()]

smallest, largest = find_largest_and_smallest(number_list)

if smallest is not None and largest is not None:
    print(f"The smallest number in the list is: {smallest}")
    print(f"The largest number in the list is: {largest}")
else:
    print("The list is empty. Please provide a list with numbers.")
