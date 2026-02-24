import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

dot = ax.scatter(0, 5, s=1000, c='skyblue')

def update(frame):
    x = frame * 0.1
    y = 5
    dot.set_offsets([x, y])
    return dot,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=100,
    interval=50,
    blit=False
)

plt.show()


