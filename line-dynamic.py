import matplotlib.pyplot as plt

x = []
y = []
n = int(input("Enter number of points: "))

for i in range(n):
    x_val = int(input(f"Enter X value {i + 1}: "))
    y_val = int(input(f"Enter X value {i + 1}: "))

    x.append(x_val)
    y.append(y_val)

plt.plot(x, y)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Dynamic Array Line Chart")

plt.show()