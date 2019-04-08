from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.


def upload_property_images(instance,filename):
    return "property/images/{}/{}".format(instance.id,filename)


class PropertyTable(models.Model):

    # The first element in each tuple is the actual value to be set
    # on the model, and the second element is the human-readable name.
    propery_type_choices = (
        ('House', 'House'),
        ('unit/flat', 'Flat'),
        ('Townhouse', 'Villa'),
    )
    propery_loc_choices = (
        ('North', 'Northern Metropoliton'),
        ('South', 'Southern Metropoliton'),
        ('East', 'Eastern Metropoliton'),
        ('West', 'Western Metropoliton'),
    )
    property_rooms_choices = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
    )
    user_data = models.ForeignKey(User)
    property_name = models.CharField(max_length=30)
    property_address = models.CharField(max_length=60)
    property_rooms = models.CharField(max_length=2,choices=property_rooms_choices,default='1')
    property_location = models.CharField(max_length=5,choices=propery_loc_choices,
                                        default="North")
    property_type = models.CharField(max_length=9,
                                    choices=propery_type_choices,
                                    default='House')
    property_pincode = models.IntegerField(default = 0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    image = models.ImageField(upload_to=upload_property_images)
    property_price = models.IntegerField(default=0)

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