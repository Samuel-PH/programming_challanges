#Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

def calculate_and_print_integer_quotient():
    try:
        first_input_number = float(input("Please enter the first number: "))
        second_input_number = float(input("Please enter the second number: "))

        quotient_without_decimal = int(first_input_number // second_input_number)
        
        print(f"The quotient without the decimal point is: {quotient_without_decimal}")
        
    except ValueError:
        print("The number you have entered is invalid")
        
    except ZeroDivisionError:
        print("You cannot divide a number by zero.")

calculate_and_print_integer_quotient()