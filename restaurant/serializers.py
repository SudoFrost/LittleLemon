from rest_framework.serializers import ModelSerializer
from .models import MenuItem, Booking

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
        read_only_fields = ('id',)

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('id',)