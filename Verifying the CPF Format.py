# CPF (Cadastro de Pessoas Físicas) is a unique taxpayer identification number
# issued by the Brazilian Federal Revenue Service to both Brazilian citizens and
# resident aliens. It consists of 11 digits and is used for tax and identification
# purposes throughout Brazil.
#
# You work in the customer service department of a company and need to quickly
# verify whether customers are entering their CPF numbers in the correct format
# before registering the data in the system.
#
# The expected CPF format is: three blocks of 3 digits separated by dots (.),
# followed by a block of 2 digits separated by a hyphen (-).
#
# Your task is to write a program that prompts the user for a CPF number and
# checks whether it is in the correct format.
#
# Input example:
#   Enter the CPF in the format XXX.XXX.XXX-XX: 123.456.789-00
#
# Expected output:
#   The CPF is in the correct format.

import re

cpf = input("Enter the CPF in the format: XXX.XXX.XXX-XX: ")
if re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
    print(f"The CPF {cpf} is in the correct format")
else:
    print(f"The CPF {cpf} is not in the correct format. Please enter a valid CPF.")