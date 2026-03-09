#Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

def print_non_duplicate_numbers():
    all_numbers = []
    
    try:
        for current_count in range(10):
            current_number = float(input(f"Enter number {current_count + 1}: "))
            all_numbers.append(current_number)
            
        print("Numbers that appear only once:")
        for number in all_numbers:

            if all_numbers.count(number) == 1:
                print(number)
                
    except ValueError:
        print("The number you have entered is invalid")

print_non_duplicate_numbers()