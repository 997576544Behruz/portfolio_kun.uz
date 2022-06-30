from django.contrib import admin
from .models import Category,Region,Tag,News
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['name',"slug"]
    prepopulated_fields={'slug':('name',)}
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display=['title','category','region']
    prepopulated_fields={'slug':('title',)}
    list_display_links=['title','category','region']
