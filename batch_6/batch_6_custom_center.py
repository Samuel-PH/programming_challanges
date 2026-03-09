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