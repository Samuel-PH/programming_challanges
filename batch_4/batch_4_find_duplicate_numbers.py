#Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

def display_duplicate_numbers():
    all_numbers = []
    printed_duplicates = []
    
    try:
        for current_count in range(10):
            current_number = float(input(f"Please enter number {current_count + 1}: "))
            all_numbers.append(current_number)
            
        print("Numbers that have duplicates:")

        for number in all_numbers:
            if all_numbers.count(number) > 1 and number not in printed_duplicates:
                print(number)

                printed_duplicates.append(number)
                
    except ValueError:
        print("The number you have entered is invalid")

display_duplicate_numbers()