# In this exercise, we need to organize the product names listed by
# sellers on an e-commerce platform. These names usually come with
# a mix of uppercase and lowercase letters, as well as unnecessary
# spaces at the beginning and end of the strings.

# We need to create an algorithm that takes a product name as input
# and standardizes it by converting all letters to lowercase and
# removing unnecessary spaces.

# Example:
# Enter the product name: White ChocoLAte
# Expected output:
# white chocolate

product_name = input('Enter a product name: ')
product_name_standard = product_name.lower().strip()
print(product_name_standard)