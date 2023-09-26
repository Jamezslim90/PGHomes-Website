from django.contrib import admin
from .models import Product, Feature, Project, ProjectFacility, HouseType



@admin.register(HouseType)
class HouseTypeAdmin(admin.ModelAdmin):
    list_display = ['house_name', 'project', 'house_specification', 'house_floor_area','units']

class HouseTypeInline(admin.StackedInline): # new
   model = HouseType



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
   
   list_display = ['name', 'hectares','purpose','location', 'status']
   inlines = [
            HouseTypeInline,
]

   
@admin.register(ProjectFacility)
class HouseFacilityAdmin(admin.ModelAdmin):
    pass

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  
  list_display = ['name', 'specification','project','location', 'available_units']


@admin.register(Feature)
class FeaturesAdmin(admin.ModelAdmin):
     pass