from rest_framework import serializers
from .models import Category,Category_color 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__str__"
        
class Category_colorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_color
        fields = "__str__"
        