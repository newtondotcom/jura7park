from rest_framework import routers
from db.derivatives import PointsViewSet

router = routers.DefaultRouter()
router.register('points', PointsViewSet)
