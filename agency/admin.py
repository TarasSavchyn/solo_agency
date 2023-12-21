from django.contrib import admin
from .models import Service, Agency, EventType, Organizer, Event, Advice, Review

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'agency_values')
    filter_horizontal = ('services',)  # Додавання фільтрації для багато-до-багатьох відносин

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'phone', 'email')
    search_fields = ('first_name', 'last_name', 'position')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_type', 'date', 'user')
    filter_horizontal = ('organizers',)  # Додавання фільтрації для багато-до-багатьох відносин

@admin.register(Advice)
class AdviceAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'rating', 'created_at', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('user__username', 'text')
