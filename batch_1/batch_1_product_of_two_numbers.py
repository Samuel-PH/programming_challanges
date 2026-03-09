#Create a program that ask user to input 2 numbers. Print the product of the two numbers.

def print_sum_of_two_numbers():
    try:
        first_input_number = float(input(f"Please enter the first number: "))
        second_input_number = float(input(f"Please enter the second number: "))

        product_of_numbers = first_input_number * second_input_number

        print(f"the product of the two numbers you have given is {product_of_numbers}")

    except ValueError:
        print("The number you have entered is invalid")

print_sum_of_two_numbers()