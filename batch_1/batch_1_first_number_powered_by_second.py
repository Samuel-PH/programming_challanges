#Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

def power_of_two_numbers():
    try:
        first_input_number = float(input(f"Please enter the first number: "))
        second_input_number = float(input(f"Please enter the second number: "))

        calculated_result = first_input_number ** second_input_number

        print(f"The result of {first_input_number} raised to the power of {second_input_number} is: {calculated_result}")

    except ValueError:
        print("The number you have entered is invalid")

    except OverflowError:
        print(" The number you entered is too big. Enter a smaller number")
        
power_of_two_numbers()