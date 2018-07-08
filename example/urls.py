from rest_framework import routers
from .views import OpenWilsonViewSet, CloseWilsonViewSet
from .views import ResultOpenWilsonViewSet, ResultCloseWilsonViewSet, ResultWilsonViewSet


router = routers.DefaultRouter()
#router.register(r'openwilson', OpenWilsonViewSet)
router.register(r'openwilson', ResultOpenWilsonViewSet, 'openwilson')
#router.register(r'closewilson', CloseWilsonViewSet)
router.register(r'closewilson', ResultCloseWilsonViewSet, 'closewilson')
router.register(r'wilson', ResultWilsonViewSet, 'wilson')
