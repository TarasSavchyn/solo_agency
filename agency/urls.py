from rest_framework.routers import DefaultRouter
from agency.views import (
    EventHallViewSet,
    EventTypeViewSet,
    EventViewSet,
    ContractorViewSet,
    OrderViewSet,
    OrganizerViewSet,
    HallOptionViewSet,
    GuestViewSet
)

router = DefaultRouter()
router.register(r'event-halls', EventHallViewSet)
router.register(r'event-types', EventTypeViewSet)
router.register(r'events', EventViewSet)
router.register(r'contractors', ContractorViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'organizers', OrganizerViewSet)
router.register(r'hall-options', HallOptionViewSet)
router.register(r'guests', GuestViewSet)

urlpatterns = router.urls

app_name = "agency"
