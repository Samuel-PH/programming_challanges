#Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

def calculate_sum_of_ten_numbers():
    total_sum = 0.0
    
    try:
        for current_count in range(10):
            current_number = float(input(f"Enter number {current_count + 1}: "))
            
            total_sum = total_sum + current_number
            
        print(f"The total sum is: {total_sum}")
        
    except ValueError:
        print("The number you have entered is invalid")

calculate_sum_of_ten_numbers()