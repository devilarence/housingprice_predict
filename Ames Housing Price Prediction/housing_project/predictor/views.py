from django.shortcuts import render
from .forms import HouseInputForm
import pickle
import numpy as np
import os
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required


# Use settings for model directory management
MODEL_DIR = settings.MODEL_DIR  # Using settings for directory management

# Load model columns and scaler once at the module level
try:
    with open(os.path.join(MODEL_DIR, 'columns.pkl'), 'rb') as f:
        model_columns = pickle.load(f)

    with open(os.path.join(MODEL_DIR, 'scaler.pkl'), 'rb') as f:
        scaler = pickle.load(f)

except FileNotFoundError as e:
    model_columns = []
    scaler = None
    print(f"Error loading model files: {e}")

def load_model(name):
    """Loads the selected model from the file system."""
    try:
        with open(os.path.join(MODEL_DIR, f'{name}.pkl'), 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None

def predict_view(request):
    prediction = None
    selected_model = 'random_forest'

    if request.method == 'POST':
        form = HouseInputForm(request.POST)
        if form.is_valid():
            selected_model = form.cleaned_data['model_choice']

            # Collect input in the correct column order
            input_values = [form.cleaned_data[col] for col in model_columns]
            input_array = np.array([input_values])

            # Scale input data
            input_scaled = scaler.transform(input_array)

            # Load the selected model
            model = load_model(selected_model)
            if model:
                prediction = model.predict(input_scaled)[0]
            else:
                prediction = "Model not found."

    else:
        form = HouseInputForm()

    return render(request, 'predictor/predict.html', {
        'form': form,
        'prediction': prediction,
        'model_name': selected_model
    })

@login_required
def dashboard_view(request):
    return render(request, 'predictor/dashboard.html')

def analytics_view(request):
    return render(request, 'predictor/analytics.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


