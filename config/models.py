from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
    STATUS_NORMAL = 1 
    STATUS_DELETE = 0

class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, 'show'),
        (STATUS_HIDE, 'hide'),
    )
    SIDE_TYPE = (
        (1, 'HTML'),
        (2, 'NEW'),
        (3, 'POULAR'),
        (4, 'Latest comm'),
    )
    title = models.CharField(max_length=50)
    display_type = models.PositiveIntegerField(default=1, choices=SIDE_TYPE)
    status = models.PositiveIntegerField(default=STATUS_SHOW, choices=STATUS_ITEMS)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural="sidebars"