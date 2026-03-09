#Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

def check_if_numbers_are_not_equal():
    try: 

        first_input_number = float(input("Please enter the first number: "))
        second_input_number = float(input("Please enter the second number: "))

        if first_input_number != second_input_number:
            print("Not Equal")
            
    except ValueError:
        print("The number you have entered is invalid")

check_if_numbers_are_not_equal()