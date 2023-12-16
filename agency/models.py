from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class EventHall(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    maximum_number_of_guests = models.IntegerField()
    options = models.ManyToManyField("HallOption", related_name="hall_options", blank=True)
    phone = models.CharField(max_length=13)
    email = models.EmailField()

    class Meta:
        ordering = ["name"]
        unique_together = ("name", "city")

    def __str__(self):
        return f"{self.name} ({self.city})"


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
    name = models.CharField(max_length=255, choices=EVENT_TYPE_CHOICES, unique=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=63)
    number_of_guests = models.IntegerField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.OneToOneField(EventType, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.IntegerField()
    contractors = models.ManyToManyField('Contractor', related_name='events', blank=True)
    style = models.ForeignKey("Style", on_delete=models.CASCADE)
    guests = models.ManyToManyField("Guest", related_name="event_guests", blank=True)

    def __str__(self):
        return f"{self.name} - {self.event_type.name}"


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

    def __str__(self):
        return self.style


class Contractor(models.Model):
    service = models.CharField(max_length=63)
    price = models.IntegerField()
    phone = models.CharField(max_length=13)
    email = models.EmailField()

    def __str__(self):
        return f"{self.service} - {self.price}"


class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order for {self.user.first_name} {self.user.last_name} - {self.event.name} on {self.date}"


class Organizer(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    position = models.CharField(max_length=63)
    events_organized = models.ManyToManyField(Event, related_name='organizers', blank=True)
    phone = models.CharField(max_length=13)
    email = models.EmailField()


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"


class HallOption(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField()

    def __str__(self):
        return self.name


SEX_CHOICES = (
    ("male", "Men"),
    ("female", "Women"),
)


class Guest(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    adult = models.BooleanField()
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    phone = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)


    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
