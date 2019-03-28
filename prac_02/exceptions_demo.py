"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter a non-zero denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    denominator = int(input("Enter a non-zero denominator: "))
    fraction = numerator / denominator
    print(fraction)
print("Finished.")

# Questions

# When will a ValueError occur?
# - When the numerator or denominator is a floating point number or string character
#
# When will a ZeroDivisionError occur?
# - When the denominator is a zero
#
# Could you change the code to avoid the possibility of a ZeroDivisionError?
# - No mathematically the output would be undefined
#