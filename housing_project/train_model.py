# enhanced_train_model.py

import pandas as pd
import numpy as np
import os
import pickle
from math import sqrt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.feature_selection import VarianceThreshold

# Load dataset
df = pd.read_csv('AmesHousing.csv')

# Drop rows with missing SalePrice
df = df.dropna(subset=['SalePrice'])

# Select numeric columns only and drop rows with missing values
df = df.select_dtypes(include=['number']).dropna()

# Drop low-variance features
selector = VarianceThreshold(threshold=1.0)
X = df.drop(columns=['SalePrice'])
X = pd.DataFrame(selector.fit_transform(X), columns=X.columns[selector.get_support()])
y = df['SalePrice']

# Drop highly correlated features (correlation > 0.95)
corr_matrix = X.corr().abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
to_drop = [column for column in upper.columns if any(upper[column] > 0.95)]
X = X.drop(columns=to_drop)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define models
models = {
    'linear': LinearRegression(),
    'ridge': Ridge(),
    'lasso': Lasso(),
    'random_forest': RandomForestRegressor(n_estimators=100, random_state=42),
    'gradient_boosting': GradientBoostingRegressor(n_estimators=100, random_state=42)
}

# Create models directory
os.makedirs('models', exist_ok=True)

# Train and save models
results = {}
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    rmse = sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    results[name] = {'rmse': rmse, 'r2': r2}
    print(f"{name} -> RMSE: {rmse:.2f}, R²: {r2:.4f}")

    # Save model
    with open(f'models/{name}.pkl', 'wb') as f:
        pickle.dump(model, f)

# Save preprocessor and columns
with open('models/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
with open('models/columns.pkl', 'wb') as f:
    pickle.dump(X.columns.tolist(), f)

# Save results
with open('models/results.pkl', 'wb') as f:
    pickle.dump(results, f)
