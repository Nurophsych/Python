import matplotlib.pyplot as plt

# First 5 cubic numbers
x_small = [1, 2, 3, 4, 5]
y_small = [x**3 for x in x_small]

# First 5000 cubic numbers
x_large = list(range(1, 5001))
y_large = [x**3 for x in x_large]

# Plot first 5 cubic numbers
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(x_small, y_small, marker='o', linestyle='-', color='blue', label='First 5 Cubic Numbers')
ax.set_title('First 5 Cubic Numbers')
ax.set_xlabel('Number')
ax.set_ylabel('Cube')
ax.legend()
plt.show()

# Plot first 5000 cubic numbers
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(x_large, y_large, color='red', linewidth=1, label='First 5000 Cubic Numbers')
ax.set_title('First 5000 Cubic Numbers')
ax.set_xlabel('Number')
ax.set_ylabel('Cube')
ax.legend()
plt.show()
