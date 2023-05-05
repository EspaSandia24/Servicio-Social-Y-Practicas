from django.urls import path
from ususarios import views

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
]