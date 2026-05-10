# You are developing a system that checks whether partner website 
# links start with https:// and end with .com. 
# These criteria are mandatory for a site to be approved during 
# registration. 
# Create a program that performs this validation automatically.
# How would you write a program that asks the user for 
# a URL and reports whether it is valid or invalid?
# Input example:
# Enter the URL for validation: https://monitorrenan.com
# Expected output:
# Valid URL!

client_URL = input("Enter the URL for validation. Exemple: https://checkinvalidation.com -> ")
if client_URL.startswith("https://") and client_URL.endswith(".com"):
    print("Valid URL!")
else:
    print("Enter a valid URL, please!")