# Difficulty: Beginner
# Scenario
# An HR system needs to identify which employees qualify for an annual performance bonus. Only employees
# earning above a certain salary threshold are eligible.
# Task
# Given the list of employee dictionaries below, use a single list comprehension to extract only the names of
# employees whose salary is greater than 50000.
# Starting Data
# employees = [
# {"name": "Arjun", "salary": 45000},
# {"name": "Priya", "salary": 72000},
# {"name": "Rahul", "salary": 55000},
# {"name": "Divya", "salary": 38000},
# ]
# Expected Output
# # Expected: ["Priya", "Rahul"]

employees = [
    {"name": "Arjun", "salary": 45000},
    {"name": "Priya", "salary": 72000},
    {"name": "Rahul", "salary": 55000},
    {"name": "Divya", "salary": 38000},
]

eligible_employees = [emp["name"] for emp in employees if emp["salary"] > 50000]

print(eligible_employees)