#Create a program that ask user to input 2 numbers. Print the bigger number.

def find_bigger_number():
    try:
        first_input_number = float(input(f"Please enter the first number: "))
        second_input_number = float(input(f"Please enter the second number: "))
        
        if first_input_number > second_input_number:
            print(f"The bigger number is { first_input_number }")

        elif second_input_number > first_input_number:
            print(f"The bigger number is { second_input_number }")
        
        else:
            print("Both of the numebers you have entered is Equal")

    except ValueError:
        print("The number you entered is invalid")

find_bigger_number()