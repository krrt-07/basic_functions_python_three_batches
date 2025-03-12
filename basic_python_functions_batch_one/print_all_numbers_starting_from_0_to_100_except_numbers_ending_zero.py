# use for-loop to print numbers from 0 to 100.
for number in range(101):
# make a condition to disregard numbers ending in zero.
    if number % 10 != 0:
# print all numbers from 0 to 100 except numbers ending in zero.
        print(number)