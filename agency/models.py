from django.db import models
from django.contrib.auth.models import AbstractUser


class Hall(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    maximum_number_of_guests = models.IntegerField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} {self.city}"


class Organizer(AbstractUser):
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EventType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField()


class Event(models.Model):
    number_of_guests = models.IntegerField
    customer = models.ManyToManyField(Customer)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    date = models.DateField()
    cost = models.IntegerField()

    def __str__(self):
        return f"{self.customer} {self.event_type.name}"
