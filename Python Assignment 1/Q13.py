def count_occurrences(input_list):
    occurrence_dict = {}  

    
    for item in input_list:
        if item in occurrence_dict:
            occurrence_dict[item] += 1  
        else:
            occurrence_dict[item] = 1     

    return occurrence_dict

user_input = input("Enter elements of the list separated by spaces: ")

input_list = user_input.split()

occurrences = count_occurrences(input_list)
print("Occurrences of each element in the list:")
for element, count in occurrences.items():
    print(f"{element}: {count}")
