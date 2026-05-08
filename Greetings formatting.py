# This exercise asks us to create a program that allows us to display,
# based on the client's name and city, greetings.
# We need to ask the client for their name and city, and after that
# show them a personalized welcome message.

# Example:
# Enter the client's name: Laura
# Enter the client's city: Denver
# Expected output: Hello, Laura! Welcome to Denver City System!

clients_name = input("Enter the client's name: ")
clients_city = input("Enter the client's city: ")
message = f"Hello, {clients_name}! Welcome to {clients_city} City System!"
print(message)