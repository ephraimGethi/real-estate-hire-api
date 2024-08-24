from rest_framework.serializers import ModelSerializer
from .models import Property,Reservation
from useraccount.serializers import UserDetailSerializer

class PropertiesListSerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = ['id','title','price_per_night','image_url']


class PropertiesDetailSerializer(ModelSerializer):
    landlord = UserDetailSerializer(read_only = True,many = False)
    class Meta:
        model = Property
        fields = ['id','title','price_per_night','image_url','bedrooms','bathrooms','guests','landlord']

class ReservationsListSerializer(ModelSerializer):
    property = PropertiesListSerializer(read_only = True,many=False)
    class Meta:
        model = Reservation
        fields = ['id','start_date','end_date','number_of_nights','total_price','property']