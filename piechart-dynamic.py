import matplotlib.pyplot as plt

n = int(input("Enter number of categories: "))

labels = []
sizes = []

for i in range(n):
    label = input(f"Enter label {i+1}: ")
    value = float(input(f"Enter value for {label}: "))
    
    labels.append(label)
    sizes.append(value)

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title(" Pie Chart (Dynamic)")
plt.show()