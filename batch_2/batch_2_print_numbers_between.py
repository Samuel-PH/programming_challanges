#Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

def print_numbers_between():
    try:
        first_input_number = int(input("Please enter the first number: "))
        second_input_number = int(input("Please enter the second number: "))

        start_number = min(first_input_number, second_input_number)
        end_number = max(first_input_number, second_input_number)

        for current_number in range(start_number + 1, end_number):
            print(current_number)

    except ValueError:
        print("The number you have entered is invalid")

print_numbers_between()