from rest_framework import routers
from django.conf.urls import url, include
from .views import NormalUserViewSet, ExpertViewSet, AdministratorViewSet

router = routers.DefaultRouter()
router.register('NormalUser', NormalUserViewSet)
router.register('Expert', ExpertViewSet)
router.register('Administrator', AdministratorViewSet)
urlpatterns = router.urls