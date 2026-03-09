#Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

def print_quotient_of_two_numbers():
    try:
        first_input_number = float(input(f"Please enter the first number: "))
        second_input_number = float(input(f"Please enter the second number: "))

        quotient_of_the_numbers = first_input_number / second_input_number

        print(f"the quotient of the two numbers you have given is {quotient_of_the_numbers}")

    except ValueError:
        print("The number you have entered is invalid")
    
    except ZeroDivisionError:
        print("Error: You cannot divide a number by zero! Please try again with a non-zero second number.")

print_quotient_of_two_numbers()