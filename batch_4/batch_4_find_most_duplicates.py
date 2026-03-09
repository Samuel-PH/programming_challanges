#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

def find_most_frequent_number():
    all_numbers = []
    
    try:
        while True:
            all_numbers.append(float(input("Please enter a number: ")))
            
    except ValueError:
        if all_numbers:

            most_frequent = max(all_numbers, key=all_numbers.count)
            print(f"The number with the most duplicates is: {most_frequent}")
            
        print("The number you have entered is invalid")

find_most_frequent_number()