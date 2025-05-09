from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from predictor.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('', RedirectView.as_view(url='/dashboard/', permanent=False)),
    path('', include('predictor.urls')),
]