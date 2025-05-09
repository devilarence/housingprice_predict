from django.urls import path
from . import views

app_name = 'predictor'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('predict/', views.predict_view, name='predict'),
    path('analytics/', views.analytics_view, name='analytics'),
]

