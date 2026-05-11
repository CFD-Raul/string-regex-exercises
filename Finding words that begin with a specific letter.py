# You work at a library and are organizing book titles in the system. You need
# to identify all titles that contain words starting with a specific letter in
# order to create thematic collections based on particular letters. For example,
# you could use this to group books whose words start with the same letter,
# helping with organization or campaigns like "Books with A for you!".
#
# Your task is to write a program that prompts the user for a text and a starting
# letter, then returns all words in the text that begin with that letter.
#
# Input example:
#   Enter the book title: Alice's Adventures in Wonderland
#   Enter the starting letter for search: A
#
# Expected output:
#   ["Alice's", "Adventures"]  # any words starting with 'A' found in the title

import re

book_title = input("Enter the book title: ")
chose_letter = input("Enter the starting letter for search: ")
chose_letter_words = re.findall(rf"\b{chose_letter}[a-zA-ZÀ-öø-ÿ]*", book_title, re.IGNORECASE)
print(chose_letter_words)