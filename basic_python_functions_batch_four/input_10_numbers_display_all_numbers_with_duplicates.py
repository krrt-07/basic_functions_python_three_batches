# Initialize an empty list to store numbers.
numbers = []
# Use for-loop and ask the user to input 10 numbers.
for i in range(10):
    number = int(input(f"Number {i+1}: "))
    numbers.append(number)
# Find numbers that have duplicates by using another for-loop.
duplicates = []
for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)
# Display only the numbers with duplicates
print(f"Duplicate numbers: {duplicates}")
