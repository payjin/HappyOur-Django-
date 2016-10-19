
from django.db import models

# Create your models here.


from django.contrib.auth.models import User



class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images/', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username

from django.db import models
#import numpy as np


class Beverage(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    upc = models.CharField(max_length=50)
    BEV_CHOICES = (
        (0, 'Beer'),
        (1, 'Wine'),
        (2, 'Liquor'),
    )

    bev = models.IntegerField(choices=BEV_CHOICES)
    def __str__(self):
        return self.name

class Review(models.Model):
    RATING_CHOICES = (
        (1, 'Awful!'),
        (2, 'No thanks!'),
        (3, 'Fine, I guess'),
        (4, 'Tasty delight!'),
        (5, 'Ambrosia of the gods!'),
    )
    name = models.ForeignKey(Beverage, null=True, blank=True)
    pub_date = models.DateTimeField('date published', null=True, blank=True)
    user_name=models.CharField(max_length=100, null=True, blank=True)
    comment = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)


