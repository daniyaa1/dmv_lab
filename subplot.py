import matplotlib.pyplot as plt


categories = ['A', 'B', 'C', 'D']
values = [10, 20, 30, 40]

plt.figure(figsize=(10,5))


plt.subplot(1, 2, 1)   
plt.bar(categories, values)
plt.title("Bar Chart")


plt.subplot(1, 2, 2)   
plt.pie(values, labels=categories, autopct='%1.1f%%')
plt.title("Pie Chart")

plt.tight_layout()
plt.show()