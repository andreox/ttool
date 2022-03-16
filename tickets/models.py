from enum import auto
from django.db import models

class Tickets(models.Model):
    id = models.AutoField(primary_key=True)
    head = models.CharField(max_length=100000, blank=True, default='')
    body = models.CharField(max_length=1000000, blank=True, default='')
    ticket_class = models.CharField(max_length=500, blank=True, default='')
    

    class Meta:
        ordering = ['id']