# For loop that displays all of the odd numbers between
# 1 and 20 with a space between each one

for i in range(1, 21, 2):
    print(i, end='  ')
print()

# For loop that counts 10 from 0 to 100

for i in range(0, 101, 10):
    print(i, end='  ')
print()

# For loop that counts down from 20 to 1

for i in range(20, 0, -1):
    print(i, end='  ')
print()

# For loop that prints n lines of increasing stars

number_of_stars = int(input(" How many stars do you want ?.."))

for i in range(1, number_of_stars+1, 1):
    string_of_stars = i * "*"
    print(string_of_stars)
print()
