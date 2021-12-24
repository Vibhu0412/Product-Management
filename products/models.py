from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    tag = models.ManyToManyField(Tag, default=False, null=True)
    image = models.ImageField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=False, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
