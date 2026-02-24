# Two-List Challenge
# Given two lists of numbers, write code to return a third list that contains only the numbers appearing in both lists — no duplicates, sorted ascending.
l1 = [11, 25, 13,84, 95, 46]
l2 = [84, 25, 46, 14, 85]

l3 = []

for n in l1:
    if n in l2 and n not in l3:
        l3.append(n)

l3.sort()

print(l3)