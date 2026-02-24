# List Comprehension
# Given a list of words, use a list comprehension to create a new list containing only the words longer than 4 characters.

words = ["car","book","apple","basket","horn","stars"]
four_words = []

for n in words:
    if len(n) > 4:
        four_words.append(n)
        print(four_words)

