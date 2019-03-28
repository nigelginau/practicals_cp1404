"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = 0
bonus = ()
while sales >= 0:
    sales = float(input("Enter sales: $"))

    if sales <= 0:
        print("No bonus available")
        bonus = 0

    elif sales < 1000:
        bonus = sales * 0.1

    else:
        bonus = sales * 0.15

    print("User bonus is ${:.2f}".format(bonus))
# ask_user_again = float(input("Enter sales: $"))

