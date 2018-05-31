from rest_framework import routers
from django.conf.urls import url, include
from .views import NormalUserViewSet

router = routers.DefaultRouter()
router.register('NormalUser', NormalUserViewSet)
urlpatterns = router.urls