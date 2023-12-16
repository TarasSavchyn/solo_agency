from rest_framework import serializers
from .models import EventHall, EventType, Event, Style, Contractor, Order, Organizer, HallOption, Guest


class HallOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallOption
        fields = ['id', 'name', 'description']


class EventHallSerializer(serializers.ModelSerializer):
    options = HallOptionSerializer(many=True, read_only=True)

    class Meta:
        model = EventHall
        fields = ['id', 'name', 'city', 'address', 'maximum_number_of_guests', 'options', 'phone', 'email']


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ['id', 'name']


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = ['id', 'style']


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = ['id', 'service', 'price', 'phone', 'email']


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'first_name', 'last_name', 'adult', 'sex']


class EventSerializer(serializers.ModelSerializer):
    contractors = ContractorSerializer(many=True, read_only=True)
    style = StyleSerializer()

    class Meta:
        model = Event
        fields = ['id', 'name', 'number_of_guests', 'customer', 'event_type', 'date', 'price', 'contractors', 'style']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'date', 'event']


class OrganizerSerializer(serializers.ModelSerializer):
    events_organized = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Organizer
        fields = ['id', 'first_name', 'last_name', 'position', 'events_organized']
