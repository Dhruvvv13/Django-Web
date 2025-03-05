from django.contrib import admin
from django.urls import path
from myapp.views import menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', menu, name='menu'),  # Route for menu page
]
