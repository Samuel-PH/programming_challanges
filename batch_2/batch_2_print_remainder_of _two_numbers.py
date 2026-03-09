#Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

def calculate_and_print_remainder():
    try:
        first_input_number = float(input("Please enter the first number: "))
        second_input_number = float(input("Please enter the second number: "))

        remainder_of_numbers = first_input_number % second_input_number
        
        print(f"The remainder is: {remainder_of_numbers}")
        
    except ValueError:
        print("The number you have entered is invalid")
        
    except ZeroDivisionError:
        print("Error: You cannot divide a number by zero.")

calculate_and_print_remainder()