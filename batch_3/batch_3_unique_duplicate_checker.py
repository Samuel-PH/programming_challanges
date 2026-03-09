#Create a program that ask user to input a number, continue asking until the user input is invalid. 
#Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

def check_for_unique_or_duplicate():
    seen_numbers = []
    
    try:

        while True:
            current_number = float(input("Please enter a number: "))
            
            if current_number in seen_numbers:
                print("Duplicate")
                
            else:
                print("Unique")
                seen_numbers.append(current_number)
                
    except ValueError:
        print("The number you have entered is invalid")

check_for_unique_or_duplicate()