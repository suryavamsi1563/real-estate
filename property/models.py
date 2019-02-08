from django.db import models
from datetime import date
# Create your models here.


def upload_property_images(instance,filename):
    return "property/images/{}/{}".format(instance.id,filename)

def upload_property_files(instance,filename):
    return "property/tax_document/%s/%s" %(instance.id,filename)

def upload_property_reg(instance,filename):
    return "property/registartion_doc/{}/{}".format(instance.property_name,filename)

def upload_property_sale(instance,filename):
    return "property/sale/{}/{}".format(instance.property_name,filename)

class PropertyTable(models.Model):

    # The first element in each tuple is the actual value to be set
    # on the model, and the second element is the human-readable name.
    propery_type_choices = (
        ('House', 'House'),
        ('unit/flat', 'Flat'),
        ('Townhouse', 'Villa'),
    )
    
    property_name = models.CharField(max_length=30)
    property_address = models.CharField(max_length=60)
    property_age = models.IntegerField(default=0)
    property_type = models.CharField(max_length=9,
                                    choices=propery_type_choices,
                                    default='House')
    property_pincode = models.IntegerField(default = 0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    tax_document = models.FileField(upload_to=upload_property_files,blank=True, null=True)
    image = models.ImageField(upload_to=upload_property_images,blank=True, null=True)
    registration_doc = models.FileField(upload_to=upload_property_reg,blank=True, null=True)
    sale_deed_image = models.ImageField(upload_to = upload_property_sale,blank=True, null=True)

    def __str__(self):
        return self.property_name

class PropertyDetails(models.Model):
    propery_parking = (
        (True, 'Available'),
        (False, 'Not Available')
    )
    propery_facing = (
        ('N', 'North'),
        ('S', 'South'),
        ('E', 'East'),
        ('W', 'West'),
    )
    property_id = models.OneToOneField(PropertyTable,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    property_area = models.IntegerField()
    property_bedroom = models.IntegerField()
    property_parking = models.BooleanField(max_length=9,
                                    choices=propery_parking,
                                    default=True)
    property_buid_year = models.DateField(default = date(1950,12,12))
    property_facing = models.CharField(max_length=9,
                                    choices=propery_facing,
                                    default='N')

class Property_Owner_Details(models.Model):
    property_id =  models.ForeignKey(PropertyTable, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=256)
    phno = models.IntegerField()
    Address = models.TextField(max_length=144)
    age = models.IntegerField()
    pan_no = models.CharField(max_length=10)

class materials(models.Model):
    name = models.CharField(max_length = 20)
    cost = models.IntegerField()

    def __str__(self):
        return self.name


class Contacted(models.Model):
    issue_choices = (
        ('SELL', 'Selling a property'),
        ('BUY', 'Buying Related'),
        ('CONTACT', 'Contacting Seller or Buyer'),
    )
    name = models.CharField(max_length=40)
    email = models.EmailField()
    mobile = models.IntegerField()
    issue_type=models.CharField(max_length=7,choices=issue_choices,default='CONTACT')
    issue = models.TextField(max_length=256)
    bot_field =models.CharField(max_length=1,blank=True, null=True)

    def __str__(self):
        return self.name