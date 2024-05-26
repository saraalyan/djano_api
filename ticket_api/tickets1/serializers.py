from rest_framework import serializers
from tickets1.models import Movie, Guest, Reservation

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
class GuestSerializer(serializers.ModelSerializer):
    reservations = ReservationSerializer(many=True, read_only=True)

    class Meta:
        model = Guest
        fields = ['pk', 'reservations', 'name', 'mobile']  # Corrected from 'reservation' to 'reservations'
