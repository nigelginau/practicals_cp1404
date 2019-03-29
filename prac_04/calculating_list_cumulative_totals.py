# Ask  for number of monthly incomes to enter
total_months = int(input('How many months ? '))
cumulative_total = [0]
# Get and store the monthly incomes in a list
for i in range(1, total_months + 1):
    income_for_month = [int(input('Enter income for month {}:'.format(i)))]
    cumulative_total = income_for_month + cumulative_total

    print("\nIncome Report\n-------------")

    for i in range(1, total_months + 1):
        print("Month {0} - Income: $  {1:10.2f}          Total: $ {1:10.2f}".format(i, cumulative_total[i - 1]))
