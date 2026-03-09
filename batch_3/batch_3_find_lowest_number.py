#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

def find_lowest_number():
    all_numbers = []
    
    try:
        while True:
            current_number = float(input("Please enter a number: "))
            all_numbers.append(current_number)
            
    except ValueError:
        if all_numbers:
            print(f"The lowest number is: {min(all_numbers)}")
            
        print("The number you have entered is invalid")

find_lowest_number()