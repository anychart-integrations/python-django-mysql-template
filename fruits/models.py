from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Fruits(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    def as_json(self):
        return dict(
            name=self.name,
            value=self.value,)
    class Meta:
        managed = False
        db_table = 'fruits'
