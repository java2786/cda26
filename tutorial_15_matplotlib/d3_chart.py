import numpy as np
import matplotlib.pyplot as plt

# print(np.__version__)
x = np.arange(1,13)
y = np.random.randint(400, 5000, 12)

print(x)
print(y)

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, y, color="red", linewidth=1, marker="x", markersize=20)

plt.show()