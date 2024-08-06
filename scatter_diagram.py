import matplotlib.pyplot as plt

# Sample data
x = [-2.4, -1, 2.4, 3,3, 7.6,9,7.6,9,13,13,15,15,15]
y = [-2.4, -1, 2.6, 2,2.6, 7.6,7.6,9,9,13,16,14,15,16]

# Create a scatter plot
plt.scatter(x, y, label='Sample Data', color='blue', marker='o')

# Add labels and title
plt.axhline(0, color='red', linestyle='--', linewidth=1)
plt.axvline(0, color='green', linestyle='--', linewidth=1)
plt.grid(True,linestyle='--',alpha=0.5)
plt.xlabel('7EEE1',color='green')
plt.ylabel('DM',color='red')
plt.title('Scatter diagram demonstartion -A.SRINIVAS')

# Add a legend
plt.legend()
legend = plt.gca().get_legend()
for text in legend.get_texts():
    text.set_color("olive")
# Show the plot
plt.show()
