from django.db import models

# Create your models here.
class Property(models.Model):

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


    def __str__(self):
        return self.property_name