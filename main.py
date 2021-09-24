import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()

ax.scatter(x_values,y_values, c=y_values, cmap=plt.cm.winter, s=10)

# Задати назву для графіка та кожної з осей.
ax.set_title("Cube numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Задати розмір  шрифту для підписів на розмітці.
ax.tick_params(axis='both', which='major', labelsize=14)

# Задати діапазон для кожної з осей.
ax.axis([0, 5100, 0, 125000000100])

plt.savefig("cube_numbers.png", bbox_inches='tight')

plt.show()