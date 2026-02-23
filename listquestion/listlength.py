#List Length

# Given the list ["cat", "dog", "rabbit", "hamster", "parrot"], print the total number of items and the last item without hardcoding the index.

animal = ["cat", "dog", "rabbit", "hamster", "parrot"]
length = len(animal)           # using length function
print(length)
print(animal[length-1])       # used length as total count and last item in the list is placed at length-1
