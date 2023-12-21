from agency.models import Service, EventType, Organizer, Event, Advice, Review, Agency
from django import forms
from django.contrib import admin


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


class AgencyAdminForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Вимикаємо можливість створення нових екземплярів
        if Agency.objects.exists():
            self.fields["name"].widget.attrs["readonly"] = True
            self.fields["description"].widget.attrs["readonly"] = True
            self.fields["agency_values"].widget.attrs["readonly"] = True
            self.fields["services"].widget.attrs["disabled"] = True


class AgencyAdmin(admin.ModelAdmin):
    form = AgencyAdminForm
    list_display = ("name", "description", "agency_values")
    filter_horizontal = ("services",)


@admin.register(Agency)
class AgencyAdminSingleton(AgencyAdmin):
    def has_add_permission(self, request):
        # Визначаємо, чи можна додавати нові екземпляри
        return not Agency.objects.exists()


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position", "phone", "email")
    search_fields = ("first_name", "last_name", "position")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "event_type", "date", "user")
    filter_horizontal = ("organizers",)


@admin.register(Advice)
class AdviceAdmin(admin.ModelAdmin):
    list_display = ("question", "answer")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "text", "rating", "created_at", "is_approved")
    list_filter = ("is_approved",)
    search_fields = ("user__username", "text")
