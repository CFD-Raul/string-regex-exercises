# Imagine that we need to create a feature for a game in which
# the player receives clues based on specific parts of a keyword.
# We need to develop a program that extracts important parts from
# every provided word.
# Code a program that asks the user for a word and shows back the
# three first and the three last letters.
# Example:
# Enter a keyword: Mysterious
# Output:
# First: Mys
# Last: ous

keyword = input("Enter a keyword, please: ")
first3 = keyword[:3]
last3 = keyword[-3:]
print(f"First: {first3}")
print(f"Last: {last3}")