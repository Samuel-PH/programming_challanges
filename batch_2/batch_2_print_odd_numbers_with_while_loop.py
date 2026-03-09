#Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

def print_odd_numbers():
    current_number = 0
    
    while current_number <= 100:
        if current_number % 2 != 0:
            print(current_number)
        
        current_number = current_number + 1

print_odd_numbers()