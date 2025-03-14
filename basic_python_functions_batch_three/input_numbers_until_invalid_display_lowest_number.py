# Initialize an empty list to store numbers.
numbers = []
# Use while loop to continue ask the user until they break the condition.
while True:
    user_input = input("Enter a number: ")
# Make condition that check if the input is not a valid integer.
    if not user_input.isdigit():
        print("Invalid input. Stopping the program.")
        break
# Convert input to integer and Add the valid number to the list.
    num = int(user_input)
    numbers.append(num)
# Find and display the lowest number.
    if numbers:
        lowest_number = min(numbers)
        print(f"The lowest number entered is: {lowest_number}")
    else:
        print("No valid numbers were entered.")