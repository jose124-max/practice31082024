from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Hotel, Room, Reservation

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'  

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    print('xDDD')
    class Meta:
        model = Reservation
        fields = '__all__'

