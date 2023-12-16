from rest_framework import serializers
from .models import EventHall, EventType, Event, Contractor, Order, Organizer, HallOption, Guest


class HallOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallOption
        fields = ['id', 'name', 'description']


class EventHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventHall
        fields = ['id', 'name', 'city', 'address', 'maximum_number_of_guests', 'options', 'phone', 'email']


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ['id', 'name']


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = ['id', 'service', 'price', 'phone', 'email']


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'first_name', 'last_name', 'adult', 'sex', 'phone', 'email']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'name',
            'number_of_guests',
            'customer',
            'event_type',
            'date',
            'price',
            'contractors',
            'style',
            'guests'
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'date', 'event']


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = ['id', 'first_name', 'last_name', 'position', 'events_organized', 'phone', 'email']
