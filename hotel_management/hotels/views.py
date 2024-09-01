from rest_framework import viewsets
import traceback
from .models import Hotel, Room, Reservation
from .serializers import HotelSerializer, RoomSerializer, ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    def create(self, request, *args, **kwargs):
        data = request.data
        user_uid = data.get('user')
        try:
            # Obtener el usuario basado en el UID
            user = User.objects.get(username=user_uid)  # Suponiendo que UID es almacenado como nombre de usuario
            print('El usuario es:')
            print(user.id)
            data['user'] = user.id
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['POST'])
def register_user(request):
    uid = request.data.get('uid')
    email = request.data.get('email')
    display_name = request.data.get('displayName')

    # Verificar si el usuario ya existe
    if User.objects.filter(username=uid).exists():
        return Response({'message': 'El usuario ya existe'}, status=status.HTTP_200_OK)

    # Crear un nuevo usuario en Django
    user = User.objects.create_user(username=uid, email=email, first_name=display_name)
    user.save()

    return Response({'message': 'Usuario registrado con éxito'}, status=status.HTTP_201_CREATED)