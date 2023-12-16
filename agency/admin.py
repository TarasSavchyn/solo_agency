from django.contrib import admin
from agency.models import (EventHall, EventType, Event, Contractor, Order, Organizer, HallOption, Guest)


@admin.register(EventHall)
class EventHallAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address', 'maximum_number_of_guests', 'phone', 'email')
    search_fields = ('name', 'city')


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer', 'event_type', 'date', 'price')
    search_fields = ('name', 'customer__first_name', 'customer__last_name', 'event_type__name')


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ('service', 'price', 'phone', 'email')
    search_fields = ('service',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'event')
    search_fields = ('user__first_name', 'user__last_name', 'event__name')


@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'phone', 'email')
    search_fields = ('first_name', 'last_name', 'position')


@admin.register(HallOption)
class HallOptionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'adult', 'sex', 'phone', 'email')
    search_fields = ('first_name', 'last_name')
