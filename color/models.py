from django.db import models


class MyModel(models.Model):

    class Meta():
        db_table = 'Product'

    image = models.ImageField(blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True)
    count_col = models.CharField(max_length=2000, default="aaa")



