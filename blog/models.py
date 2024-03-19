from collections.abc import Iterable
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from datetime import datetime
from authentication.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(db_index=True, blank=True, max_length=250)
    title = models.CharField(max_length=250)
    views = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now())
    content = models.TextField()
    
    def save(self, *args, **kwargs) :
        self.slug  = slugify(self.title)
        return super().save(*args, **kwargs)
    
    