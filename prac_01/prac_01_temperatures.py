"""

CP1404/CP5632 - Practical

Pseudocode for temperature conversion

"""

MENU = ('C - Convert Celsius to Fahrenheit\n'
        '\n'
        'F - Convert Fahrenheit to Celsius\n'
        '\n'
        'Q - Quit')

print(MENU)

choice = input(">>> ").upper()

while choice != "Q":

    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        fahrenheit = float(input("Fahrenheit: "))
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        celsius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:.2f} C".format(celsius))
        # Remove the "pass" statement when you are done. It's a placeholder.

    else:
        print("Invalid option")

    print(MENU)

    choice = input(">>> ").upper()

print("Thank you.")
