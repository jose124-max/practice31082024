from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, RoomViewSet, ReservationViewSet
from .views import register_user

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register_user'),
]
