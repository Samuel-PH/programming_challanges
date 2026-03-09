#Create a program that ask user to input 2 numbers. Print the smaller number.

def find_and_print_smaller_number():
    try:
        first_input_number = float(input("Please enter the first number: "))
        second_input_number = float(input("Please enter the second number: "))

        if first_input_number < second_input_number:
            print(f"The smaller number is: {first_input_number}")
            
        elif second_input_number < first_input_number:
            print(f"The smaller number is: {second_input_number}")
            
        else:
            print("Both numbers are equal.")
            
    except ValueError:
        print("The number you have entered is invalid")

find_and_print_smaller_number()