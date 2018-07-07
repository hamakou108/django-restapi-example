from django.db import models


class OpenWilson(models.Model):
    item_id = models.CharField(max_length=8)
    open_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)


class CloseWilson(models.Model):
    item_id = models.CharField(max_length=8)
    close_date = models.DateTimeField(auto_now_add=True)
