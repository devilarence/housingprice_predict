import pickle
import os
from django import forms

MODEL_DIR = 'models'

# Load model columns
with open(os.path.join(MODEL_DIR, 'columns.pkl'), 'rb') as f:
    model_columns = pickle.load(f)

# Define available models
MODEL_CHOICES = [
    ('random_forest', 'Random Forest'),
    ('ridge', 'Ridge Regression'),
    ('lasso', 'Lasso Regression'),
    ('linear', 'Linear Regression'),
    ('gradient_boosting', 'Gradient Boosting'),
]

class HouseInputForm(forms.Form):
    # Define a choice field for model selection
    model_choice = forms.ChoiceField(
        choices=MODEL_CHOICES,
        label='Select Model',
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Dynamically add fields based on the model columns
        for col in model_columns:
            # Apply custom attributes for better field rendering in templates
            self.fields[col] = forms.FloatField(
                label=col.replace('_', ' ').title(),
                required=True,
                widget=forms.NumberInput(attrs={
                    'step': 'any', 
                    'class': 'w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500'
                })
            )
