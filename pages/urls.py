from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, InvestmentPageView, GalleryPageView


urlpatterns = [

path('',  HomePageView.as_view() , name='home'),
path('about/',  AboutPageView.as_view() , name='about'),
path('contact/',  ContactPageView.as_view() , name='contact'),
path('investment/',  InvestmentPageView.as_view() , name='investment'),
path('gallery/',  GalleryPageView.as_view() , name='gallery'),

]
