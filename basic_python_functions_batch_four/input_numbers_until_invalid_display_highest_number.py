# Initialize an empty list to store numbers.
numbers = []
# Use while loop to continue ask the user while the condition is true.
while True:
    user_input = input("Enter a number: ")
# Check if the input is not a valid integer.
    if not user_input.isdigit():
        print("Invalid input. Stopping the program.")
        break
# Convert input to integer.
    num = int(user_input)
# Add the valid number to the list.
# find the Highest number of all of the numbers by making a condition and using maximum "max()" and print it.