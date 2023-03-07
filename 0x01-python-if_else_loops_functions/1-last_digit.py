#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 # get the last digit using modulo operator
print("Last digit of", number, "is", last_digit) # print the output
if last_digit > 5: # check if last digit is greater than 5
    print("and is greater than 5")
elif last_digit == 0: # check if last digit is zero
    print("and is 0")
else: # otherwise last digit is less than 6 and not zero
    print("and is less than 6 and not 0")
