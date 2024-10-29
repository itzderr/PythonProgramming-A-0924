from oop.transaction import Transaction
import datetime as dt

t1 = Transaction(dt.datetime(2024, 10, 1), "Food", "Grocery", 50.75, "Expense")
t2 = Transaction(dt.datetime(2024, 10, 2), "Rent", "Monthly Rent", 1200, "Expense")
t3 = Transaction(dt.datetime(2024, 10, 2), "Utilities", "Electricity Bill", 60, "Expense")
print(t1.get_category())
t1.set_category("qoifjwioajkldsl;kajsdf")
print(t1.get_category())

# total amount
monthly_transactions = [t1, t2, t3]
total = 0
for t in monthly_transactions:
    total += t.get_amount()

print(total)

# filter transaction by category
food = []
for t in monthly_transactions:
    if t.get_category() == "Food":
        food.append(t)


food[0].set_type("Income")
print(food[0].get_type())



