import matplotlib.pyplot as plt  # Import pyplot

input_values = [1, 4, 9, 16, 25]
squares = [20,2,77,52,99]

plt.style.use('seaborn-v0_8-dark-palette')
fig, ax = plt.subplots()  # Use plt.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.set_title('Square Numbers', fontsize = 24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(labelsize=14)
 

plt.show()  # Use plt.show()
