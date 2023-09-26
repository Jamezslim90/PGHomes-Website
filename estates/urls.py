from django.urls import path
from .views import  ProjectListView, ProjectDetailView,ProductListView, ProductDetailView

urlpatterns = [

path('project/',  ProjectListView.as_view() , name='project_listing'),
path('project/<int:pk>/', ProjectDetailView.as_view() , name='project_detail'),
path('product/', ProductListView.as_view() , name='product_listing'),
path('product/<int:pk>/', ProductDetailView.as_view() , name='product_detail'),
]

