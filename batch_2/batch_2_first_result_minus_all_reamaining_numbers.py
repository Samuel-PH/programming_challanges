#Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

def calculate_first_minus_remaining():
    try:
        result_total = float(input("Enter number 1: "))
        
        for current_count in range(1, 10):
            current_number = float(input(f"Enter number {current_count + 1}: "))
            
            result_total = result_total - current_number
            
        print(f"The result is: {result_total}")
        
    except ValueError:
        print("The number you have entered is invalid")

calculate_first_minus_remaining()