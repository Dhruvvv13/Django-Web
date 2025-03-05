from django.shortcuts import render
from .models import Menu

def menu(request):
    menu_items = Menu.objects.all()  # Fetch all menu items
    items_dict = {"menu": menu_items}  # Pass data to template
    return render(request, "menu.html", items_dict)
