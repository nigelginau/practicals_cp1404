# A shop requires a small program that would allow them
# to quickly work out the total price for a number of items,..
# each with different prices..
# Number of items: 3
# Price of item: 100
# Price of item: 35.56
# Price of item: 3.24
# Total price for 3 items is $124.92


number_of_items = int(input("Number of items:.."))
while number_of_items < 0:
    print('Invalid ')
    number_of_items = int(input("Number of items:.."))

for i in range(1, number_of_items+1, 1):
    price_of_item = float(input("Price of item: $"))
    total_price = price_of_item()
print()
