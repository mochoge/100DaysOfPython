#Calculator to calculate the tip amount to be paid.
print("Welcome to the Tip calculator")
tip_percent = int(input("Enter the Tip percent 5,10,15 or 20: "))
bill_amount = float(input("Enter Bill amount: "))
number_of_people = int(input("Enter the number of people to split bill: "))
total_bill = bill_amount * (1 + (tip_percent/100))
print(f"The total bill is: Ksh {round(total_bill, 2)} and each person will pay a total of Ksh {round((total_bill/number_of_people),2)}")