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
# Find and display the lowest number.