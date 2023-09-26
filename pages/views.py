
# Create your views here.


from django.views.generic import TemplateView 



class HomePageView(TemplateView):

    template_name = 'pages/home.html'



class AboutPageView(TemplateView):
    
    template_name = 'pages/about.html'



class ContactPageView(TemplateView):
    
    template_name = 'pages/contact.html'


class InvestmentPageView(TemplateView):
    
    template_name = 'pages/investment.html'


class GalleryPageView(TemplateView):
    
    template_name = 'pages/gallery.html'