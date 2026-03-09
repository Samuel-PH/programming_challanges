#Create a program that ask user to input 2 numbers. Print the difference of the two numbers.

def calculate_and_print_difference():
    try:
        first_input_number = float(input("Please enter the first number: "))
        second_input_number = float(input("Please enter the second number: "))

        difference_of_numbers = first_input_number - second_input_number
        
        print(f"The difference between the numbers is: {difference_of_numbers}")
        
    except ValueError:
        print("The number you have entered is invalid")

calculate_and_print_difference()