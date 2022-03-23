from django.db import models
from cloudinary.models import CloudinaryField
from email.mime import image
from django.contrib.auth.models import User
class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )  
    body = models.CharField(
        'Body', blank=True, null=True, max_length=140, db_index=True
    )
    image = CloudinaryField (
        'image', blank=True, db_index=True
    )
    like_count = models.PositiveBigIntegerField('like_count', default=0, blank=True)
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )