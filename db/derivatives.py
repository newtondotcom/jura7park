from rest_framework import viewsets

from jura7park.models import points
from jura7park.serializers import PointsSerializer

from django.db.models import IntegerField, Value
class PointsViewSet(viewsets.ModelViewSet):
    queryset = points.objects.all().order_by('-point').annotate(rank=Value(0, IntegerField()))
    serializer_class = PointsSerializer
