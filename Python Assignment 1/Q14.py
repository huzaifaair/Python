def find_second_largest(numbers):
    
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None  

    unique_numbers.sort(reverse=True)

    return unique_numbers[1]

user_input = input("Enter numbers separated by spaces: ")

number_list = [float(num) for num in user_input.split()]

second_largest = find_second_largest(number_list)

if second_largest is not None:
    print("The second largest number in the list is:", second_largest)
else:
    print("There are not enough unique numbers to determine the second largest.")
