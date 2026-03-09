#Create a program that ask user to input 10 numbers. Print how many are even numbers.

def count_even_numbers():
    even_number_count = 0
    
    try:
        for current_count in range(10):
            current_number = int(input(f"Enter number {current_count + 1}: "))
            
            if current_number % 2 == 0:
                even_number_count = even_number_count + 1
                
        print(f"Total even numbers entered: {even_number_count}")
        
    except ValueError:
        print("The number you have entered is invalid")

count_even_numbers()
