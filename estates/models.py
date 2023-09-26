# Create your models here.
from django.db import models
from django.utils import timezone
from django.urls import reverse
import uuid
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class ProjectFacility (models.Model):
    """Model representing a project facilities."""
    
    name = models.CharField(max_length=200, help_text='Enter a product feature (e.g. Swimming-pool CCTV Solar-power)')

    class meta :
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"


    def __str__(self):
        """String for representing the Model object."""
        return self.name





class Project (models.Model):
        """Model representing a project."""

        name = models.CharField(max_length=250)
       

        description = models.TextField(max_length=1000, help_text='Enter a brief description of the project')
        location = models.CharField(max_length=300)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        hectares = models.DecimalField(max_digits=6, decimal_places=1, help_text="Enter the number of hectares",null=True, blank=True,)
        
        facilities = models.ManyToManyField(ProjectFacility, help_text='Select a feature for this project')
        image= models.ImageField(upload_to='images/')

    

        PROJECT_STATUS = (
        ('Not started', 'Not started'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
    )

        status = models.CharField(
        max_length=50,
        choices= PROJECT_STATUS,
        blank=True,
        default='Not started',
        help_text='Project work status',
    )

        PROJECT_PURPOSE = (
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Others', 'Others'),
    )

        purpose = models.CharField(
        max_length=50,
        choices= PROJECT_PURPOSE,
        blank=True,
        default='Residential',
        help_text='Project purpose',
    )

        class meta :
            ordering = ['-name'] 
            verbose_name = 'Projects'

    
        def __str__(self):
            """String for representing the Model object."""
            return self.name
        
        def get_absolute_url(self):

            """Returns the URL to access a detail record for this project."""
            return reverse('project_detail', args=[str(self.id)])





class HouseType (models.Model):

    """Model representing a project HouseType."""

    house_name = models.CharField(max_length=250, null= True, blank= True)
    house_specification = models.CharField(max_length=300, help_text='Enter a brief specification of the product')
    house_floor_area = models.PositiveBigIntegerField(help_text="Enter the net floor area for the product")
    units = models.PositiveIntegerField(null= True, blank=True)
    house_outright_payment = models.DecimalField(max_digits=12, decimal_places=2, help_text="Enter the outright payment price", default= 0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='housetypes')
    image= models.ImageField(upload_to="images/", default=True)
    bed= models.PositiveIntegerField(help_text="Enter the number of bedroom", default=1)
    bath= models.PositiveIntegerField(help_text= "Enter the Number of bathroom", default=1)

    HOUSETYPE_STATUS = (
        ('For Rent', 'For Rent'),
        ('For Sale', 'For Sale')
    )

    status= models.CharField(
        max_length =50,
        choices = HOUSETYPE_STATUS,
        blank=True,
        default='For Sale',
        help_text='House Type Status'
    )

    class meta :
            ordering = ['-house_name'] 
            verbose_name = 'HouseTypes'

    
    def __str__(self):
            """String for representing the Model object."""
            return self.house_name
        
        
        




class Feature (models.Model):
    """Model representing a product feature."""
    
    name = models.CharField(max_length=200, help_text='Enter a product feature (e.g. Fan Kitchen-cabinet wardropes)')

    class meta :
        verbose_name_plural = 'Features' 


    def __str__(self):
        """String for representing the Model object."""
        return self.name



class Product(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    name = models.CharField(max_length=250, null= True, blank= True)
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    title_document = models.CharField(max_length=250, null= True, blank= True)
    description = models.CharField(max_length= 250, null= True, blank=True)
    # Foreign Key used because product can only have one project, but project can have multiple products
  
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)

    specification = models.CharField(max_length=300, help_text='Enter a brief specification of the product')
    location = models.CharField(max_length=300, help_text="Enter a the product location")
    bedrooms = models.PositiveIntegerField(null= True, blank=True)
    bathrooms= models.PositiveIntegerField(null= True, blank=True)
    payment_duration = models.PositiveIntegerField(help_text="Enter a number in months e.g 18")
    available_units = models.PositiveIntegerField(null= True, blank=True)
    features = models.ManyToManyField(Feature, help_text='Select a feature for this product')
    outright_payment = models.DecimalField(max_digits=12, decimal_places=2, help_text="Enter the outright payment price", default= 0)
    mortgage_payment = models.DecimalField(max_digits=12, decimal_places=2, help_text="Enter the mortgage payment price",  default= 0)
    installmental_payment = models.DecimalField(max_digits=12, decimal_places=2, help_text="Enter installmental payment price",  default= 0)
   
    floor_area = models.PositiveBigIntegerField(help_text="Enter the net floor area for the product")
    image= models.ImageField(upload_to='images/')
    
    SALES_STATUS = (
        ('Sold Out', 'Sold Out'),
        ('Now Selling', 'Now Selling'),
        ('On Request', 'On Request'),
        ('Not Available', 'Not Available'),
    )

    sales = models.CharField(
        max_length=50,
        choices= SALES_STATUS,
        blank=True,
        default='Now Selling',
        help_text='Product sales status',
    )

    TYPE_STATUS = (
         ('Land', 'Land'),
        ('Building', 'Building'),
    )
    
    type = models.CharField(
        max_length=50,
        choices= TYPE_STATUS,
        blank=True,
        default='Building',
        help_text='Product type status',
    )

    class meta :
        ordering = ['-name']
        verbose_name = 'Products'


    def __str__(self):
        """String for representing the Model object."""
        return self.name

    

