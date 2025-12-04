from atexit import register
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet,Category_colorViewSet

router = DefaultRouter()
router = register('Category',CategoryViewSet)
router = register('Category_color',CategoryViewSet)

ulpatterns = [
 path("",include(router.urls))
]