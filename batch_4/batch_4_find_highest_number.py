#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

def find_highest_number():
    all_numbers = []
    
    try:
        while True:
            all_numbers.append(float(input("Please enter a number: ")))
            
    except ValueError:
        if all_numbers:
            print(f"The highest number is: {max(all_numbers)}")
            
        print("The number you have entered is invalid")

find_highest_number()