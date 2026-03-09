#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

def sort_numbers_ascending():
    all_numbers = []
    
    try:
        while True:
            all_numbers.append(float(input("Please enter a number: ")))
            
    except ValueError:
        all_numbers.sort()
        print(all_numbers)
        
        print("The number you have entered is invalid")

sort_numbers_ascending()