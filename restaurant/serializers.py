from rest_framework.serializers import ModelSerializer
from .models import Menu, Booking

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        read_only_fields = ('id',)

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        read_only_fields = ('id',)