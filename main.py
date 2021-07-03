import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()

ax.scatter(x_values,y_values, s=10)

plt.show()