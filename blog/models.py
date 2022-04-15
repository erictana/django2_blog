from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'normal'),
        (STATUS_DELETE, 'deleted'),
    )

    name = models.CharField(max_length=50, null=False, blank=False )
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS)
    is_nav = models.BooleanField(default=False)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    created_time= models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'normal'),
        (STATUS_DELETE, 'deleted'),
    )
    name = models.CharField(max_length=50, null=False, blank=False )
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    created_time= models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'normal'),
        (STATUS_DELETE, 'deleted'),
        (STATUS_DRAFT, 'draft'),
    )

    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=1024, blank=True, null=True)
    content = models.TextField(help_text='must be mark down')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, 
            choices=STATUS_ITEMS)
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    tag = models.ManyToManyField(Tag)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now_add=True)
    
    class Meta:
            ordering = ['-id']