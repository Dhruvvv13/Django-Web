from django.http import HttpResponse

def drinks(request, drink_name):
    # Step 3: Create dictionary with drink descriptions
    drink = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment',
    }

    # Step 4: Get the description based on the drink name
    choice_of_drink = drink.get(drink_name, "Drink not found")

    # Step 5: Return the HTTP response
    return HttpResponse(f"<h2>{drink_name}</h2>{choice_of_drink}")
