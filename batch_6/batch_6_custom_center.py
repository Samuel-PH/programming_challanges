#center() add space characters at the beginning and at the end of the string to print the string at the center. 
#Create a program that do the same functionality without using center() function.

def custom_center():
    text = input("Please enter your text: ")
    
    try:
        target_width = int(input("Enter the total width needed: "))
        text_length = len(text)
        
        if target_width > text_length:
            total_padding = target_width - text_length
            left_pad = total_padding // 2
            right_pad = total_padding - left_pad
            centered_text = (" " * left_pad) + text + (" " * right_pad)
            
            print(f"Result: [{centered_text}]")
            
        else:
            print(f"Result: [{text}]")
            
    except ValueError:
        print("Please enter a valid whole number for the width.")

custom_center()

#optimized

def custom_center():
    try:
        text = input("text:")
        width = int(input("width:"))
        pad = max(0, (width - len(text)) // 2)
        print(f"Result: [{' ' * pad + text + ' ' * pad}]")
    except ValueError:
        print("invalid width")

custom_center()

#STEPS:
#1. Get input from the user for the text and the desired total width.   
#2. Calculate the length of the input text.
#3. If the desired width is greater than the length of the text, calculate the total padding needed and divide it into left and right padding.
#4. Create the centered text by adding the left padding, the original text, and the right padding together.
#5. Print the result with brackets to visualize the centering.