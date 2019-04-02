def main():
    # Ask  for number of monthly incomes to enter
    total_months = int(input('How many months ? '))
    income_list = [0]
    # Get and store the monthly incomes in a list
    for i in range(1, total_months + 1):
        income_for_month = [int(input('Enter income for month {}:'.format(i)))]
        income_list = income_list + income_for_month

    print("\nIncome Report\n-------------")

    for i in range(1, total_months + 1):
        cumulative_total = sum(income_list[:i + 1])
        print("Month {0} - Income: $  {1:10.2f}          Total: $ {2:10.2f}".format(i, income_list[i], cumulative_total))
main()
