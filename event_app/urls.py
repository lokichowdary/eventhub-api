from rest_framework.routers import DefaultRouter
from .views import EventViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = router.urls