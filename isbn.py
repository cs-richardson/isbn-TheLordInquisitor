'''
This programs check if an ISBN number is valid.
---Program written by Son Nguyen---
'''
#Define how many digits is in an ISBN variable
ISBN_DIGIT = 10

#Initialize the total value as 0 and prompt the user for an input
total = 0
user_input = int(input("Input an ISBN number for validation: "))

#For each digit, find the value of each digit and calculate the total
for i in range(ISBN_DIGIT):
    number = user_input % 10
    number_value = number * (ISBN_DIGIT - i)
    total = total + number_value
    user_input = user_input // 10

#Print whether or not the value is considered an ISBN number
if total % 11 == 0:
    print("Valid. This is an ISBN number.")
else:
    print("Invalid. This is not an ISBN number.")



