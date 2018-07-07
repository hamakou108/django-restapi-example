from rest_framework import routers
from .views import ResultViewSet, OpenWilsonViewSet, CloseWilsonViewSet


router = routers.DefaultRouter()
router.register(r'openwilson', OpenWilsonViewSet)
router.register(r'closewilson', CloseWilsonViewSet)
