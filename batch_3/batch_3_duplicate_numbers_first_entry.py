#Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

def display_first_entries_only():
    seen_numbers = []
    
    try:
        for current_count in range(10):
            current_number = float(input(f"Enter number {current_count + 1}: "))
            
            if current_number not in seen_numbers:
                seen_numbers.append(current_number)
                
        print(f"The unique first entries are: {seen_numbers}")
        
    except ValueError:
        print("The number you have entered is invalid")

display_first_entries_only()