from rest_framework import viewsets
from .models import EventHall, EventType, Event, Contractor, Order, Organizer, HallOption, Guest
from .serializers import EventHallSerializer, EventTypeSerializer, EventSerializer, ContractorSerializer, OrderSerializer, OrganizerSerializer, HallOptionSerializer, GuestSerializer

class EventHallViewSet(viewsets.ModelViewSet):
    queryset = EventHall.objects.all()
    serializer_class = EventHallSerializer

class EventTypeViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ContractorViewSet(viewsets.ModelViewSet):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer

class HallOptionViewSet(viewsets.ModelViewSet):
    queryset = HallOption.objects.all()
    serializer_class = HallOptionSerializer

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
