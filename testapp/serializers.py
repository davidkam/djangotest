from django.contrib.auth.models import User
from testapp.models import Amenity
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class AmenitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Amenity
        fields = ('eng_name', 'chi_name', 'icon')
