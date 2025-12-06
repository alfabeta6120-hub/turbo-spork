from .models import Category,CategoryColor
from .serialisers import CategorySerializer,CategoryColorSerializer
from rest_framework import viewsets

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryColorViewSet(viewsets.ModelViewSet):
    queryset = CategoryColor.objects.all()
    serializer_class = CategoryColorSerializer
    

