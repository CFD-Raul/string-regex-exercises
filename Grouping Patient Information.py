# You are a data analyst at a hospital and are organizing
# patient information in a database. You receive the data
# in the format: "FirstName LastName - Year".
# For example: "Monalisa Silva - 1994".
#
# You need a program that reads this information and
# extracts each part separately: first name, last name,
# and year of birth, in order to populate system fields.
#
# Create a program that asks for a patient's full name
# and year of birth, and then displays them separately.
#
# Input Example:
#
# Enter the patient's full name and year of birth:
# Ana Silva - 1990
#
# Expected Output:
#
# First Name: Ana
# Last Name: Silva
# Year of Birth: 1990

import re


patient_data = input("Enter the patient's full name and year of birth in the format (First Name Last Name - Year): ")
pattern = r'(\w+) (\w+) - (\d{4})'

result = re.search(pattern, patient_data)

if result:
    first_name = result.group(1)
    last_name = result.group(2)
    year_of_birth = result.group(3)
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Year of Birth: {year_of_birth}")

else:
    print("Invalid format!")