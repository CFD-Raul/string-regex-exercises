# You are a writer reviewing a text for publication. During the process, you noticed
# that you used the word "good" repeatedly, when you wanted to express something
# stronger, like "great". To save time, you want to automatically replace all
# occurrences of the word "good" with "great" in the text.
# Create a program that asks for a text, the word to be replaced, and the new word.
# The program should display the text with the changes applied.
# Input example:
# Enter the text to be reviewed: The day is good, everything is good.
# Which word do you want to replace? good
# What is the new word? great
# Expected output:
# The day is great, everything is great.

import re

text = input("Enter the text to be reviewed: ")
word_to_replace = input("Which word do you want to replace? ")
new_word = input("What is the new word? ")
new_text = re.sub(rf"\b{word_to_replace}\b", new_word, text)
print(new_text)