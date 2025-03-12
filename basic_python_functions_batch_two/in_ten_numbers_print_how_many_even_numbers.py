# set count to 0 and set sum to 0.
code = 0
sum = 0
# make a while loop that will run ten times to ask for a number.
while code < 10:
    code += 1
    number = int(input("Enter a number: "))
    # make a condition to check if the number is even and list it.
    if number % 2 == 0:
        sum += 1
# print the counted even numbers.
print(sum)
