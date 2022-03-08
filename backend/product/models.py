from django.db import models
from user.models import WishList

# Create your models here.
class Product(models.Model):
    name = models.CharField(blank=True, max_length = 150)
    description = models.TextField(blank=True)
    inv_num = models.IntegerField(null = True)
    wishlist_of = models.ForeignKey(WishList, on_delete=models.DO_NOTHING, blank = True, null=True)


