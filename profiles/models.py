from django.db import models
from django.contrib.auth.models import User
from property.models import PropertyTable


# Create your models here.
class UserProfile(models.Model):
    occupation_choice = (
        ('Private','Private'),
        ('Public','Public'),
        ('Self','Self-Employed')
    )

    # Relationship
    user = models.OneToOneField(User)

    # Custom Fields
    address = models.CharField(max_length=60)
    listed_properties = models.ForeignKey(PropertyTable,
                                        related_name='list_prope_user',
                                        blank=True,
                                        on_delete=models.CASCADE,
                                        null=True)
    contacted_properties = models.ForeignKey(PropertyTable,
                                        related_name='contact_prop_user',
                                        blank=True,
                                        on_delete=models.CASCADE,
                                        null=True)
    mobile_no = models.IntegerField()
    pan_no = models.CharField(max_length=10)
    Occupation = models.CharField(max_length=7,choices=occupation_choice,default='Public')

    def __str__(self):
        return self.user.username