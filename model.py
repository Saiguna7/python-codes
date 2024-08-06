import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the data from the CSV file
data = pd.read_csv(r'C:Users\saigu\OneDrive\Desktop\Salary_Data.csv')

# Extract the independent variable (YearsExperience) and dependent variable (Salary)
X = data[['YearsExperience']]
y = data['Salary']

# Create and fit the linear regression model
regression = LinearRegression()
regression.fit(X, y)

# Predict salaries based on the model
predicted_salaries = regression.predict(X)

# Plot the actual data points
plt.scatter(X, y, color='blue', label='Actual Data')

# Plot the regression line
plt.plot(X, predicted_salaries, color='red', label='Regression Line')

# Customize the plot
plt.title('Salary vs Experience(Training Dataset)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary in Rupees')
plt.legend()

# Show the plot
plt.show()
