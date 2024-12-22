from rest_framework import serializers
from jura7park.models import points

class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = points
        fields = '__all__'
