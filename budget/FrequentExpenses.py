import Expense #why not from.import
import collections
import matplotlib.pyplot as plt
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv') #why is it a string?
spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)
spending_counter = collections.Counter(spending_categories)
#print(spending_counter)
top5 = spending_counter.most_common(5)
categories, count = zip(*top5) # would be error if they switched because zip() always go after = sign
fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show() 
