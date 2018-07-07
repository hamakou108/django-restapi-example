from django.db import models


class Result(object):
    def __init__(self, *args, **kwargs):
        self.result_code = kwargs.get('result_code')
        self.error_code = kwargs.get('error_code')
        self.total_num = kwargs.get('total_num')
        self.info = kwargs.get('info')


class OpenWilson(models.Model):
    item_id = models.CharField(max_length=8)
    open_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)


class CloseWilson(models.Model):
    item_id = models.CharField(max_length=8)
    close_date = models.DateTimeField(auto_now_add=True)
