# Create a text file called "numbers.txt"(You can create a simple text file in
# PyCharm with Ctrl+N,  choose "File" and save it in your project). Put the numbers
# 17 and 42 on separate lines in the file and save it:17 42. Write a program that opens "numbers.txt",
# reads the numbers and adds them together then prints the result, which should be... 59

open_file = open('numbers.txt', 'r')

first_line = int(open_file.readline())
second_line = int(open_file.readline())
total = first_line + second_line

print("{0} + {1} = {2}".format(first_line, second_line, total))
