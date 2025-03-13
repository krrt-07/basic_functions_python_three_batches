# set numbers to empty set.
numbers = []
# Ask the user to input 10 numbers.
for i in range(10):
    num = int(input(f"Number {i+1}: "))
# make condition to get the only the first entry.
    if num not in numbers:
        numbers.append(num)
# Display the numbers (only first occurrences of duplicates).
print("Numbers with duplicates removed (only first entry kept):")
print(*numbers)