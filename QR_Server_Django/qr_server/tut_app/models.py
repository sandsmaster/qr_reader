from django.db import models
from datetime import date

# Create your models here.
class Ads(models.Model):
    store_name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=500)
    num_limit = models.IntegerField()
    date_limit = models.DateField(default=date.today())

    def all_for_loc(loc):
        return [item for item in Ads.objects.all() if loc in item.location]