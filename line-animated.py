import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

x = np.linspace(0, 2*np.pi, 100)

y = np.sin(x)

line, = ax.plot(x, y)

ax.set_ylim(-2, 2)
ax.set_xlim(0, 2*np.pi)

def update(frame):
    y = np.sin(x + frame * 0.1)  
    line.set_ydata(y)
    return line,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=100,
    interval=50,
    blit=True
)

plt.show()

