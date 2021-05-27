from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):

    def __str__(self):
        return self.item_name

    # given to superuser by default (we always create superuser first)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500, default='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.WbhJPOi8PiEDjZuFpEthMwHaE8%26pid%3DApi&f=1')

    # executed after any crud
    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
