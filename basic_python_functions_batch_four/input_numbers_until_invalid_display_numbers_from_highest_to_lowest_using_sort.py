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
    numbers.append(num)
# Sort the list from highest to lowest.
numbers.sort(reverse=True)
# Display the numbers from highest to lowest.
if numbers:
    print("Numbers from highest to lowest:")
    print(numbers)