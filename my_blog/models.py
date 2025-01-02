from django.db import models
from django.utils import timezone

defaultBody="Lorem ipsum dolor sit amet, consectetur adipiscing elit"

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(default=defaultBody)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-created"]
    