# John works as an attendant at a pharmacy and needs to check if a customer provided
# a valid prescription number in a description. The prescription number is always
# the only number present in the text provided by the customer. He wants a program
# that extracts this number directly and confirms whether the text is correct,
# without the need to work with lists or loops.
# Based on this scenario, create a program that receives a text with a description
# and displays a message with the number found.
# Input example:
# Enter the prescription description: The prescription 1087568 was sent by the customer.
# Expected output:
# The prescription number is: 1087568

import re

prescription_message = input("Enter the prescription description: ")
prescription_number = re.search(r"\d+", prescription_message)
if prescription_number:
    print("The prescription number is:", prescription_number.group())
else:
    print("The prescription you entered is not valid. Please enter a valid prescription.")