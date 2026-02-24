import matplotlib.pyplot as plt

n = int(input("Enter number of points: "))

x = []
y = []

for i in range(n): 
    x_val = float(input("Enter x values {i + 1}: "))
    y_val = float(input("Enter y values {i + 1}: "))

    x.append(x_val)
    y.append(y_val)

plt.scatter(x, y)

plt.title("Scatter Plot (Dynamic)")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()
