# Initialize an empty list to store numbers.
numbers = []
# Use while loop to continue ask the user until they break the condition.
while True:
    user_input = input("Enter a number: ")
# Check if the input is not a valid integer.
    if not user_input.isdigit():
        print("Invalid input. Stopping the program.")
        break
# Convert input to integer.
    num = int(user_input)
# Add the valid number to the list.
    numbers.append(num)
# Sort the list from lowest to highest.
numbers.sort()
# Display the sorted numbers.