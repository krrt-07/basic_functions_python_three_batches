# set count and sum to 0.
count = 0
sum = 0
# make a while loop that will run ten times to ask the user for a number.
while count < 10:
    # asd for a number.
    number = int(input("Enter a number: "))
    count += 1
# make a condition to check if the number is odd.
    if number % 2 != 0:
    # make a command that will count how many odd numbers is there.
        sum += 1
# print the count of odd numbers.
print(sum)