from rest_framework import serializers
from .models import Category,CategoryColor 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class CategoryColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryColor
        fields = "__all__"
        