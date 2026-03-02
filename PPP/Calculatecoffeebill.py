# Difficulty: Beginner
# Scenario
# You are working as a barista at a coffee shop. At the end of each order you need to calculate the total bill by
# applying a sales tax on top of the item subtotal.
# Task
# Write a function called calculate_bill that accepts three parameters: item_price (float), quantity (int), and
# tax_rate (float). The function should return the final bill amount as a float after applying the tax to the
# subtotal.
# Expected Output
# calculate_bill(4.50, 3, 0.08) # Expected: 14.5



def calculateCoffeeBill(item_price:float, quantity:int,tax_rate:float) -> float:
    totalCoffeeBill = item_price * quantity
    tax_rate = tax_rate * 100
    finalCoffeeBill = totalCoffeeBill + tax_rate
    return finalCoffeeBill

print(calculateCoffeeBill(4.50, 3, 0.08))