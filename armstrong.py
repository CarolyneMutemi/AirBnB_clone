#!/usr/bin/python3

lower = 100
upper = 1000

for num in range(lower, upper+1):
    # Order of number
    power = len(str(num))

    # Initializing sum
    sum = 0

    rem_digits = num

    while rem_digits > 0:
        # Get each digit in num
        digit = rem_digits % 10
        sum += digit ** power
        rem_digits //= 10  # Remaining digits in num

    if num == sum:
        print(num)
