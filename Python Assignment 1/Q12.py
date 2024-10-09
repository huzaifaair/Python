def remove_duplicates(input_list):
    unique_list = []  
    seen = set()      

    for item in input_list:
        if item not in seen:  
            unique_list.append(item)  
            seen.add(item)            

    return unique_list

user_input = input("Enter elements of the list separated by spaces: ")

input_list = user_input.split()

unique_list = remove_duplicates(input_list)
print("The list after removing duplicates is:", unique_list)
