# Initialize an empty list to store numbers.
numbers = []
# Use while loop to continue ask the user while the condition is true.
while True:
    user_input = input("Enter a number: ")
# Make a condition that will check if the input is not a valid integer.
    if not user_input.isdigit():
        print("Invalid input. Stopping the program.")
        break
# Convert input to integer.
    num = int(user_input)
# Add the valid number to the list.
    numbers.append(num)
# Find the number with the most duplicates by making a condition using maximum "max()" and print it.