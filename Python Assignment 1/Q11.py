def reverse_list(input_list):
    
    reversed_list = []
    
    for i in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[i])
    
    return reversed_list

user_input = input("Enter elements of the list separated by spaces: ")

input_list = user_input.split()

reversed_list = reverse_list(input_list)
print("The reversed list is:", reversed_list)
