from django.db import models
from utils.abstract_model import Model


class Company(Model):
    name = models.CharField(max_length=255)
    icon_url = models.URLField()
    page_links = models.JSONField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
    
