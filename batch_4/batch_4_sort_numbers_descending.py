#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function
def sort_numbers_descending():
    all_numbers = []
    
    try:
        while True:
            all_numbers.append(float(input("Please enter a number: ")))
            
    except ValueError:
        if all_numbers:
            all_numbers.sort(reverse=True)
            print(f"Numbers from highest to lowest: {all_numbers}")
            
        print("The number you have entered is invalid")
        
sort_numbers_descending()