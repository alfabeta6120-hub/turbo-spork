from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet,CategoryColorViewSet

router = DefaultRouter()
router.register('Category',CategoryViewSet)
router.register('CategoryColor',CategoryColorViewSet)

urlpatterns = [
 path("",include(router.urls))
]