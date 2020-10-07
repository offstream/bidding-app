from django.db import models
from django.contrib.auth import get_user_model

from apps.utils.models import Timestamps
from datetime import datetime, timedelta


def default_expirydate():
    return datetime.now() + timedelta(days=7)


class Product(Timestamps, models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=150)
    description = models.TextField(default='', blank=True)
    image = models.ImageField(
        upload_to='product-images', default=None, null=True, blank=True)
    min_price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    max_price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    expiry_date = models.DateTimeField(default=default_expirydate)

    def __str__(self):
        return self.name
