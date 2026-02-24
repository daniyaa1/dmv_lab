import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

x = []
n = int(input("Enter number of values: "))

for i in range(n):
    val = int(input(f"Enter value {i + 1}: "))
    x.append(val)

x = np.array(x)

fig, ax = plt.subplots()
bins = np.linspace(min(x), max(x), 10)

def update(frame):
    ax.clear()
    ax.hist(x[:frame], bins=bins, edgecolor='black')
    ax.set_xlabel("Values")
    ax.set_ylabel("Frequency")
    ax.set_title("Dynamic Histogram (User Input)")

ani = FuncAnimation(fig, update, frames=range(1, len(x) + 1), interval=500)

plt.show()
