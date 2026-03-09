#Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

def print_numbers_not_ending_in_zero():
    for current_number in range(101):
        
        if current_number % 10 != 0:
            print(current_number)

print_numbers_not_ending_in_zero()