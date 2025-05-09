# 🏡 Ames Housing Price Prediction Web App

- **Source**: [Ames Housing Dataset](https://www.kaggle.com/datasets/prevek18/ames-housing-dataset)
- **Attributes**: The dataset contains 80+ variables describing various aspects of residential homes in Ames, Iowa.
- **Target**: `SalePrice` – the final price of the house.

Only **numeric** columns are used in training to ensure compatibility and simplify preprocessing. Missing values are dropped for cleaner model inputs.

---

## 🤖 ML Model Training

Training was done in `enhanced_train_model.py` using the following steps:

1. **Data Cleaning**: Drop missing `SalePrice` values and non-numeric columns.
2. **Feature Selection**:
   - Remove low-variance features (variance < 1.0).
   - Drop highly correlated features (correlation > 0.95).
3. **Scaling**: StandardScaler is applied to normalize the input features.
4. **Model Training**:
   - `Linear Regression`
   - `Ridge Regression`
   - `Lasso Regression`
   - `Random Forest`
   - `Gradient Boosting`
5. **Model Evaluation**: Models are scored using RMSE and R² metrics.
6. **Saving Artifacts**:
   - Trained models (`.pkl`)
   - Scaler (`scaler.pkl`)
   - Feature column names (`columns.pkl`)
   - Evaluation results (`results.pkl`)

---

## 🔐 Authentication

- **Built-in Django authentication system** is used.
- Users must sign in to:
  - Make predictions
  - View their prediction history
  - Access analytics dashboards

---

## 🔄 Django Integration

- **Backend**: Python, Django, Django REST Framework
- **Frontend**: HTML, TailwindCSS, Chart.js
- **Features**:
  - Upload features or manually input house data
  - Select from multiple trained models
  - View results and prediction statistics
  - Save predictions in browser (localStorage) or database
  - Analytics dashboard with charts for:
    - Price prediction over time
    - Price distribution
    - Model performance

---

## 📦 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/ames-housing-predictor.git
cd ames-housing-predictor

# Set up virtual environment
pip install pipenv
pipenv install

# Activate environment
pipenv shell

# Run migrations
python manage.py migrate

# Train models (optional)
python enhanced_train_model.py

# Start the server
python manage.py runserver
