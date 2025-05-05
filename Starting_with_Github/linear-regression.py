from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data: X = feature, y = target
X = np.array([[1], [2], [3], [4], [5]])  # feature
y = np.array([3, 5, 7, 9, 11])          # target

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Predict
X_new = np.array([[6], [7]])
predictions = model.predict(X_new)

print("Predictions for 6 and 7:", predictions)
print("Slope (coefficient):", model.coef_)
print("Intercept:", model.intercept_)
