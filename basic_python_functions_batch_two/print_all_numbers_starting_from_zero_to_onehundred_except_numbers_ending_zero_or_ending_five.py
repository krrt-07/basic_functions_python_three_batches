# set count and sum equal to 0.
count = 0
sum = 0

# use while loop to run 100 times.
while count < 100:
    count += 1
    sum += 1
    # make condition to disregard numbers ends with 0 or 5.
    if sum % 10 != 0 or sum % 5 != 0:
        # print the number.