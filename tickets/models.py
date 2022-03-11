from enum import auto
from django.db import models

class Tickets(models.Model):
    id = models.AutoField(primary_key=True)
    head = models.CharField(max_length=100, blank=True, default='')
    body = models.CharField(max_length=300, blank=True, default='')
    ticket_class = models.CharField(max_length=50, blank=True, default='')
    

    class Meta:
        ordering = ['id']