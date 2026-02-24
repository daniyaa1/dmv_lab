import matplotlib.pyplot as plt
import numpy as np

x = np.array([2, 4, 4, 5, 6, 6, 6, 7, 8, 9, 10])

plt.hist(x, bins=7, edgecolor='black')
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Static Histogram (Predefined Array)")
plt.show()