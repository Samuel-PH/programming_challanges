#Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

def print_numbers_skipping_zero_and_five():

    for current_number in range(101):
        
        if current_number % 10 != 0 and current_number % 10 != 5:
            print(current_number)

print_numbers_skipping_zero_and_five()