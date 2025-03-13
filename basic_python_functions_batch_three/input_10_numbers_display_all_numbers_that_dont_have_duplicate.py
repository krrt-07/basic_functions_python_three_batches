# Ask the user to input 10 numbers.
numbers = []
for i in range(10):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

# Find numbers that appear only once.
unique_numbers = [num for num in numbers if numbers.count(num) == 1]
# Display the unique numbers