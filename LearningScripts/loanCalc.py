
owed: float = float(input("How much do you owe in US dollars?\n"))

apr: float = float(input("What's the annual percentage rate?\n"))

payment = float(input("What will your monthly payment be in dollars?\n"))

months = int(input("How many months do you want to see results for?\n"))

monthly_rate = apr/100/12

for i in range(months):

    interest_paid = owed * monthly_rate
    owed = owed + interest_paid

    if (owed - payment < 0):
        print("The last payment is", owed)
        print("You paid off the loan in", i+1, "months")
        break

    owed = owed - payment

    print("Paid", payment, "of which", interest_paid, "was interest", end=" ")
    print("Now I owe", owed)
