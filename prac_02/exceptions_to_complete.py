"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
print("Find the product of two factors")
first_factor = second_factor = 0
while not finished:
    try:
        first_factor = int(input("Input first factor which must be a integer : "))
        second_factor = int(input("Input second factor which must be a integer : "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")

result = first_factor * second_factor
print("Valid result is:", result)
