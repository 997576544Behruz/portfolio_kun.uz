from turtle import title
from unicodedata import category, name
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50,unique=True)
    def __str__(self):
        return self.name
class Region(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50,unique=True)
    def __str__(self):
        return self.name
class News(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True)
    content=models.TextField()
    img=models.ImageField(upload_to='news/%Y/%m/%d')
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    region=models.ForeignKey(Region,on_delete=models.SET_NULL,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    views_count=models.IntegerField(default=0)
    update_at=models.DateTimeField(auto_now=True)
    tag=models.ManyToManyField('Tag')
class Tag(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50,unique=True)
    def __str__(self):
        return self.name
