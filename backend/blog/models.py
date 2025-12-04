from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Category_color(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=True)
    
    def __str__(self):
        return self.name

