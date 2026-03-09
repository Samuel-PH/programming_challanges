#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. 
#Create a program that do the same functionality without using ljust() function.

def custom_left_justify():
    text = input("Please enter your text: ")
    
    try:
        target_length = int(input("Enter the total number of characters needed: "))
        justified_text = text
        
        while len(justified_text) < target_length:
            justified_text += " "

        print(f"Result: [{justified_text}]")
        
    except ValueError:
        print("Please enter a valid whole number for the length.")

custom_left_justify()