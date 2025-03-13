# Ask the user to input 10 numbers.
numbers = []
for i in range(10):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)
# Find numbers that appear only once.
# Display the unique numbers