
from models import Category,Category_color
from .serialisers import CategorySerializer,Category_colorSerializer
from rest_framework import viewsets

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class Category_colorViewSet(viewsets.ModelViewSet):
    queryset = Category_color.objects.all()
    serializer_class = Category_colorSerializer
    

