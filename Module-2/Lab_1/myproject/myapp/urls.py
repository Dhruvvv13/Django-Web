from django.urls import path  # Import path function
from . import views  # Import views from the same directory

urlpatterns = [
    path('', views.home, name="home"),  # URL pattern for home view
]
