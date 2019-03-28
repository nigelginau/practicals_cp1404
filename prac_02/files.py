# Write a program that asks the user for their name,
# then opens a file called "name.txt" and writes that name to it.

# Write user's name to text file's title

text_file_name = open('name.txt', "w")
user_name = (input(" Please enter your name to a text file: "))
print(user_name, file=text_file_name)
text_file_name.close()

# Write a program that opens "name.txt"
# and reads the name (as above) then prints
# "Your name is Bob" (or whatever the name is in the file).
read_file = open('name.txt', "r")
name = read_file.read()
print(("Your name is {}".format(name)))
read_file.close()
