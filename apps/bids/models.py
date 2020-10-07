from django.db import models
from django.contrib.auth import get_user_model

from apps.products.models import Product
from apps.utils.models import Timestamps


class Bid(Timestamps, models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    is_accepted = models.BooleanField(default=False)
