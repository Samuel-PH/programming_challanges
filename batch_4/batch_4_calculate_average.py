#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

def calculate_average():
    all_numbers = []
    
    try:
        while True:
            all_numbers.append(float(input("Please enter a number: ")))
            
    except ValueError:
        if all_numbers:
            average = sum(all_numbers) / len(all_numbers)
            print(f"The average is: {average}")
            
        print("The number you have entered is invalid")

calculate_average()