from django.urls import path
from .views import *

urlpatterns=[
    path('',home1,name="home1"),
    path('category/<slug:slug>',category_news,name="category"),
    path('region/<slug:slug>',region_news,name="region_news"),
    path('more_news/<slug:slug>',more_news,name="more_news")
]