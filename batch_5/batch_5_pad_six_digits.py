#Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

def format_number_with_zeros():
    try:
        user_number = int(input("Please enter a number (0-1000): "))
        
        if 0 <= user_number <= 1000:
            
            print(f"Formatted output: {user_number:06d}")
            
        else:
            print("Error: Please make sure the number is between 0 and 1000.")
            
    except ValueError:
        print("The number you have entered is invalid")

format_number_with_zeros()