from rest_framework import routers

from .places.views import RegionViewSet

router = routers.DefaultRouter()
router.register(r"regions", RegionViewSet)

urlpatterns = router.urls
