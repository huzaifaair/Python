print("Enter the number to check its positive, negative or zero value")
userInput = int(input())

if(userInput == 0):
    print("The number is nor positive and negative :" , userInput)
    
elif(userInput > 0 ):
    print("The number is positive :" , userInput)

else:
    print("The number is negative :" , userInput)