""""  Nigel Ginau """

""""write a program that asks the user for a password, with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
The program should then print asterisks as long as the password.
Example: if the user enters "Pythonista" (10 characters), the program should print "**********"."""""

minimum_length = 5
length_of_password = 0

while length_of_password < minimum_length:
    password = input("Please input your password :")
    length_of_password = len(password)
    print("Password must be more than {0} characters and greater than {1} characters".format(minimum_length,
                                                                                             length_of_password))

print("Password is the correct length of {} characters".format(minimum_length))
asterisks = length_of_password * "*"
print(asterisks)
