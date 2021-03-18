from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# class User(AbstractUser):
#     pass

class Client(models.Model):
    short_name = models.CharField(max_length=64, unique=True, blank=True, null=True)
    full_name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    tax_number = models.PositiveBigIntegerField(max_length=10,unique=True)
    industry = models.CharField(max_length=64)
    website = models.CharField(max_length=64)
    source_lead = models.CharField(max_length=64)
    status = models.CharField(max_length=32)

    created = models.DateField(auto_now_add=True)

    # person = models.ForeignKey(Person, on_delete=models.CASCADE)
    # owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)  # klient moze nie miec opiekuna
    def __str__(self):
        return f'{self.short_name}'


class Person(models.Model):
    surname = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    phone_number = models.BooleanField(default=False)
    email = models.EmailField(max_length=64)
    position = models.CharField(max_length=64)
    notes = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

# class Owner(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE) #każdy agent możemy mieć tylko 1 usera
