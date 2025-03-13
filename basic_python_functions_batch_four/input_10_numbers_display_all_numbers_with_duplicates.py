# Initialize an empty list to store numbers.
numbers = []
# Use for-loop and ask the user to input 10 numbers.
for i in range(10):
    number = int(input(f"Number {i+1}: "))
    numbers.append(number)
# Find numbers that have duplicates by using another for-loop.
duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
# Display only the numbers with duplicates
