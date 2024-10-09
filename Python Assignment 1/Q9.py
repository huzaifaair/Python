def count_vowels(input_string):
   
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0  

    for char in input_string:
        if char in vowels:  
            count += 1

    return count

user_input = input("Enter a string: ")

vowel_count = count_vowels(user_input)
print(f"The number of vowels in the given string is: {vowel_count}")
