from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Sample data: X = feature, y = target
X = np.array([[1], [2], [3], [4], [5]])  # feature
y = np.array([3, 7, 13, 21, 31])        # target (non-linear)

# Create polynomial features (degree 2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Fit the model
model = LinearRegression()
model.fit(X_poly, y)

# Predict
X_new = np.array([[6], [7]])
X_new_poly = poly.transform(X_new)
predictions = model.predict(X_new_poly)

print("Predictions for 6 and 7:", predictions)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
