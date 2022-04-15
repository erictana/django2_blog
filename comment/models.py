from django.db import models
from blog.models import Post

class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'normal'),
        (STATUS_DELETE, 'deleted'),
    )

    target = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024, blank=False, null=False)
    nickname = models.CharField(max_length=128)
    website = models.URLField()
    email = models.EmailField()
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS)
    created_time = models.DateTimeField(auto_now_add=True)

