from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    stripe_customer_id = models.CharField(max_length=50)

    def __str__(self):
        return self.name
