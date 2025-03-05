from django.db import models

class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name  # Makes it readable in admin panel

class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, default=None)
