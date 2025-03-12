# set count to 0 and set sum to 0
count = 0
sum = 0
# make a while loop that will run ten times to ask the user for a number.
while count < 10:
    # ask for a number.
    number = int(input("Enter a number:"))
    count += 1
# make a command that add all numbers.
    sum += number
# print the sum of all numbers.
print(sum)