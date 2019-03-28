"""

CP1404/CP5632 - Practical

Broken program to determine score status

"""

# TODO: Fix this!


score = float(input("Enter score: "))

if 100 > score < 0:
    print("Invalid score")

elif 90 > score > 50:
    print("Passable")

elif 100 >= score > 90:
    print("Excellent")

elif score < 50:
    print("Bad")
