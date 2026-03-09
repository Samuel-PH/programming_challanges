#Create a program that ask user to input 10 numbers. Print how many are odd numbers.

def count_odd_numbers():
    odd_number_count = 0
    
    try:

        for current_count in range(10):
            
            current_number = int(input(f"Enter number {current_count + 1}: "))
            
            if current_number % 2 != 0:
                odd_number_count = odd_number_count + 1
                
        print(f"Total odd numbers entered: {odd_number_count}")
        
    except ValueError:
        print("Invalid input. Please make sure to enter valid whole numbers.")

count_odd_numbers()