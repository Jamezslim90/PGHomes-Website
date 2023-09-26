from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Product, Project


class ProductListView (ListView):
    model: Product
    context_object_name = 'product_list' 

    template_name= 'products/product_list.html'

    def get_queryset(self):
          return Product.objects.order_by('pk')




class ProductDetailView (DetailView):
    model: Product
    context_object_name = 'product' 
    template_name = 'products/product_detail.html'

    def get_queryset(self):
          return Product.objects.order_by('pk')
        



class ProjectListView (ListView):
    model: Project
    context_object_name = 'project_list' 
    template_name= 'projects/project_list.html'

    def get_queryset(self):
          return Project.objects.order_by('pk')


    


class ProjectDetailView (DetailView):

    model: Project
    context_object_name = 'project' 
   
    template_name= 'projects/project_detail.html'

    def get_queryset(self):
          return Project.objects.order_by('pk')
