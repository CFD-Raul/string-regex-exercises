# Lorena works in the registration department of a company and needs to ensure
# that the names entered by customers are in the correct format. The expected
# pattern is that names start with an uppercase letter and contain only letters
# (no numbers or special characters). To simplify her workflow, she wants a
# program that automatically validates the provided names.
#
# Help Lorena by creating a program that prompts the user for a name and checks
# whether it meets the rules.
#
# Input example:
#   Enter the customer name for validation: maria123
#
# Expected output:
#   Invalid name!

import re

client_name = input("Enter the client's name for validation: ")
if re.fullmatch(r'[A-ZÀ-Ö][a-zA-ZÀ-öø-ÿ]+( (da|de|do|das|dos|e)| [A-ZÀ-Ö][a-zA-ZÀ-öø-ÿ]+)*', client_name):
    print(f"The name {client_name} is a valid name!")
else:
    print(f"The name {client_name} is an invalid name. Please enter a valid name.")