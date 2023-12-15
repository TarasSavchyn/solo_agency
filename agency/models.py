from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class EventHall(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    maximum_number_of_guests = models.IntegerField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} {self.city}"


EVENT_TYPE_CHOICES = (
    ("corporate", "Corporate"),
    ("wedding", "Wedding"),
    ("first_date", "First Date"),
    ("stag", "Stag"),
    ("girls_party", "Girls Party"),
    ("working_meeting", "Working Meeting"),
    ("birthday", "Birthday"),
    ("christening_of_a_child", "Christening of a child"),
)


class EventType(models.Model):
    name = models.CharField(max_length=255, choices=EVENT_TYPE_CHOICES)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    confirmed = models.BooleanField()


class Event(models.Model):
    name = models.CharField(max_length=63)
    number_of_guests = models.IntegerField()
    customer = models.OneToOneField('Customer', on_delete=models.CASCADE)
    event_type = models.ForeignKey('EventType', on_delete=models.CASCADE)
    date = models.DateField()
    price = models.IntegerField()
    contractors = models.ManyToManyField('Contractor', related_name='events', blank=True)
    styles = models.ManyToManyField('Style', related_name='events', blank=True)
    participants = models.ManyToManyField('User', related_name='events', blank=True)

    def __str__(self):
        return f"{self.customer} {self.event_type.name}"


STYLE_CHOICES = (
    ('white', 'White'),
    ('black', 'Black'),
    ('pink', 'Pink'),
    ('green', 'Green'),
    ('blue', 'Blue'),
    ('gray', 'Gray'),
    ('mafia', 'Mafia'),
)


class Style(models.Model):
    style = models.CharField(max_length=20, choices=STYLE_CHOICES)


class Contractor(models.Model):
    service = models.CharField(max_length=63)
    price = models.IntegerField()
