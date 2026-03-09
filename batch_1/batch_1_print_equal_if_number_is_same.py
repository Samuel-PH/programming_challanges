#Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

def checks_if_number_is_equal_number ():
    try:
        first_input_number = float(input(f"Please enter the first number: "))
        second_input_number = float(input(f"Please enter the second number: "))
            
        if first_input_number == second_input_number:
             print(f"Both of the numbers you have entered are equal.")

        else:
             print(f"Both of the numbers you have entered are not equal.")

    except ValueError:
        print("The number you entered is invalid")

checks_if_number_is_equal_number ()
