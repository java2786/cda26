import matplotlib.pyplot as plt

x_data = [1,2,3,4]
y_prices = [99, 205, 50, 150]

plt.plot(x_data, y_prices)
plt.title("Sales Data")
plt.xlabel("Month")
plt.ylabel("Profit (INR)")
plt.show()