from django.http import HttpResponse  # Import HttpResponse

def home(request):  # Define a view function
    return HttpResponse("<h1>Welcome to Little Lemon!</h1>")
