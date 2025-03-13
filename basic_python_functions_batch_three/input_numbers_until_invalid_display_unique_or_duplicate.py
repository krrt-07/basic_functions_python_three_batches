# Initialize an empty list to store numbers.
numbers = []
# Use while loop to continue ask the user until they break the condition.
while True:
    user_input = input("Enter a number: ")
# Make condition that check if the input is not a valid integer.
    if not user_input.isdigit():
        print("Invalid input. Stopping the program.")
        break
# Convert input to integer.
    num = int(user_input)
# Check if the number is already in the list.
# print the number.
    if num in numbers:
        print("Duplicate")
    else:
        print("Unique")
        numbers.append(num)