from django.contrib import admin
from .models import *


# Register your models here.

class CategoryModelAdmin(admin.ModelAdmin):
	list_display = ['id', 'name',  'timestamp']
	class Meta:
		model = Category
admin.site.register(Category, CategoryModelAdmin)

class SubCategoryModelAdmin(admin.ModelAdmin):
	list_display = ['tracker', 'name',  'timestamp']
	class Meta:
		model = Sub_category
admin.site.register(Sub_category, SubCategoryModelAdmin)

class ProductsModelAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'timestamp']
	class Meta:
		model = Products
admin.site.register(Products, ProductsModelAdmin)