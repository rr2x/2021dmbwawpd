from rest_framework import serializers
from .models import Moviedata


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moviedata
        #fields = Moviedata.getAttributeList()
        fields = ['id', 'name', 'duration', 'rating']
